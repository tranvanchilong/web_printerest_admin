from starlette.responses import PlainTextResponse, Response, JSONResponse, StreamingResponse
from resources import templates, jwt_decode, async_rq
from auth_.users import authenticate, get_user_session, get_user
from starlette.background import BackgroundTask
from resources import templates, wait_first_task
import arrow
import time
import json
import traceback
from resources import templates
import asyncio
from modules import pin_handle
from bson import ObjectId

import xml.etree.ElementTree as ET
import datetime
from db import MongoAsyncPipeline
from settings import DB 
import asyncio
from bson import ObjectId


# @authenticate
# async def homepage(request):
#     data = {}
#     return templates.TemplateResponse('index.html', {'request': request, "data": data})
@authenticate
async def by_product(request):
    data = {}
    return templates.TemplateResponse('by_product.html', {'request': request, "data": data})


async def get_all_language(request, db, str):

        list_language = []
        collection_names = await db.select_all_collections()
        for lang_a in collection_names:
            if f"{str}" in  lang_a:
                list_language.append(lang_a)
        return list_language


# hàm check lang đã edit xong hay chưa
async def check_complete_page(request, lang):
        db_client = request.state.db
        find_ = {}
        # print(lang)
        posts = await db_client.find_many(find_, f'lang_{lang}', filter_=None)
        # print(posts)
        check=0
        for document in posts:
            # print(document["lang_status"])
            if document["lang_status"] == "True":
                check=check+1
            # print(check)
        if check==len(posts):
            return("True")
        else :
            return("False")


async def sitemap(request): 
    db_client = request.state.db
    find_ = {}
    list_lang = await db_client.find_many(find_, 'list_lang', filter_=None)
    name = await get_all_language(request, db_client, "lang")

    list_true=[]
    list_false=[]

    for lang in list_lang:
        if f'lang_{lang["lang"]}' in name:
            list_true.append(lang["lang"])
        else:
            list_false.append(lang["lang"])

    today = datetime.date.today()
    urls=[]
    for lang in list_true:
        urls.append({'loc': f'https://pinterestdownloader/{lang}',    'lastmod': f'{today}'})
    # print (urls)
    headers = {'Content-Type': 'application/xml'}
    context = {
        "request": request,
        "urls":urls
    }
    return templates.TemplateResponse("sitemap.xml.j2", context, media_type='application/xml')


async def homepage(request):
    t0 = time.time()
    data = {}
    if request.method == "POST":
        form_data = await request.form()
        url = form_data['url']
        
        # check db
        db_client = request.state.db
        find_ = {'url': url}
        check = await db_client.find_one(find_, 'data', filter_=None)
        if check == None:
            tasks = [
                asyncio.create_task(pin_handle.pin_handle_data_2(url)),
                asyncio.create_task(pin_handle.pin_handle_data(url)),
            ]
            data = await wait_first_task(tasks)
            
            insert_data = {
                'url': url,
                'data': data
            }
            insert = await db_client.insert_one(insert_data, 'data')
            print(f"insert: {insert}")
        else:
            data = check['data']
            print(f"data: {data}")
    

    try:
        language=request.path_params["language"]
    except:
        language="en"

    db_client = request.state.db
    find_ = {"type": "template_menu"}
    list_menu = await db_client.find_one(find_, f'lang_{language}', filter_=None)
    # print(list_menu)
    # print()
    # print(language)
    find_ = {"type": "template_page"}
    posts = await db_client.find_one(find_, f'lang_{language}', filter_=None)
    find_={}
    list_lang = await db_client.find_one(find_, 'list_lang', filter_=None)
    langs={}
    # check lang đã edit xong
    for key in list_lang:
        if key != "_id":
        # print(key)
            if await check_complete_page(request , key) =="False":
                langs.update({key : list_lang[key]})
    # print(langs)
    # print(posts)
    context = {
        "request": request,
        "data": data,
        "posts": posts,
        "langs": langs,
        "list_menu": list_menu,
        "language": language
    }
    # print(posts)
    # print(asyncio.create_task(pin_handle.pin_handle_data(url)))
    print(f"total: {time.time() - t0} - data: {data}")
    return templates.TemplateResponse("index_2.html", context)

async def pin_get(request):
    t0 = time.time()
    form_data = await request.json()
    url = form_data['url']
    
    # check db
    db_client = request.state.db
    find_ = {'url': url}
    check = await db_client.find_one(find_, 'data', filter_=None)
    if check == None:
        tasks = [
            asyncio.create_task(pin_handle.pin_handle_data_2(url)),
            asyncio.create_task(pin_handle.pin_handle_data(url)),
        ]
        data = await wait_first_task(tasks)
        
        insert_data = {
            'url': url,
            'data': data
        }
        insert = await db_client.insert_one(insert_data, 'data')
        print(f"insert: {insert}")
    else:
        data = check['data']
    print(data)
    print(f"total: {time.time() - t0} - data: {data}")
    return JSONResponse(data)
        
# hàm tạo db
from settings import list_lang 
async def main(request):
    # C:\Users\Thong\Documents\testweb\test\t_web_tiktokdownloader\app\add_db.py
    print("xong")
    db_client = MongoAsyncPipeline(DB['DB_HOST'], DB['DB_NAME'])
  
    #     print(f"link_res {traceback.format_exc()} await func")
    # await db_client.insert_one(sknu_link, "lang_demo")
    # await db_client.insert_one(posts2_2, "lang_demo")
    # await db_client.insert_one(posts2_3, "lang_demo")
    # await db_client.insert_one(posts2_4, "lang_demo")
    # await db_client.insert_one(posts2_5, "lang_demo")
    await db_client.insert_one(list_lang, "list_lang")
    print("done")



async def show_menu(request):
    data = {}
    try:
        language=request.path_params["language"]
    except:
        language="en"

    menu=request.path_params["menu"]
    db_client = request.state.db
    find_ = {"handle": menu}
    posts = await db_client.find_one(find_, f'lang_{language}', filter_=None)

    find_ = {"type": "template_menu"}
    list_menu = await db_client.find_one(find_, f'lang_{language}', filter_=None)
    # print (posts)

    langs={}
    for key in list_lang:
        if key != "_id":
        # print(key)
            if await check_complete_page(request , key) =="False":
                langs.update({key : list_lang[key]})

    context = {
        "request": request,
        "data": data,
        "posts": posts,
        "list_menu": list_menu,
        "langs":langs
        
    }
    return templates.TemplateResponse("menu_template.html", context)