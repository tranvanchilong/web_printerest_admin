from starlette.responses import PlainTextResponse, RedirectResponse
from .resources import templates, hash_password, show_session, encode_url, jwt_decode
from .users import authenticate, login, logout, register, get_user_session, get_users, get_user, add_user, edit_user, delete_user, get_groups, get_group, add_group, edit_group, delete_group, add_route, get_routes, get_route, edit_route, delete_route, update_route_to_gorups
from starlette.responses import PlainTextResponse, Response, JSONResponse, StreamingResponse
# from resources import templates, jwt_decode, async_rq
from auth_.users import authenticate, get_user_session, get_user
from starlette.background import BackgroundTask
import arrow
import time
import json
import traceback
import asyncio
from modules import pin_handle
from bson import ObjectId

# from markupsafe import Markup   

@authenticate

 # lấy list name tất cả ngôn ngữ đẫ được tạo từ colection db str="lang"
async def get_all_language(request, db, str):
        list_language = []
        collection_names = await db.select_all_collections()
        for lang_a in collection_names:
            if f"{str}" in  lang_a:
                list_language.append(lang_a)
        return list_language
    
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

async def homepage_edit(request):
    t0 = time.time()
    data = {}
    language="en"

    db_client = request.state.db
    find_ = {}
    filter_ = {"_id": 1, "name": 1} 
    # lấy all document lang_en
    posts = await db_client.find_many(find_, 'lang_en', filter_=filter_)
    # lấy list all language
    list_lang = await db_client.find_one(find_, 'list_lang', filter_=None)

    # lấy list name tất cả ngôn ngữ đẫ được tạo từ colection db str="lang"
    name = await get_all_language(request, db_client, "lang")

    list_true={}
    list_false={}

    # check lang trong list lang có nằm trong số nn đã được tạo thì trả về list true
    # for key in list_lang:
    #     if f'lang_{key}' in name:
    #         list_true.append(list_lang[key])
    #     elif key !="_id":
    #         list_false.append(list_lang[key])
    
    # check lang trong list lang có nằm trong số nn đã được tạo thì trả về list true
    for key in list_lang:
        if f'lang_{key}' in name:
            if await check_complete_page(request, key)=="True":
                key2="Đã chỉnh sửa"
            else:
                key2="Chưa chỉnh sửa"
            list_true.update({key:{"lang":list_lang[key],"status":key2}})
        elif key !="_id":
            # if await check_complete_page(request, key)=="True":
            #     key2="True"
            # else:
            key2="None"
            list_false.update({key:{"lang":list_lang[key],"status":key2}})

    context = {
        "request": request,
        "data": data,
        "list_true": list_true,
        "list_false":list_false
    }

    print(f"total: {time.time() - t0} - data: {data}")
    return templates.TemplateResponse("homepage_edit.html", context)

@authenticate
async def show_list_page(request):
    t0 = time.time()
    data = {}
    language=request.path_params["language"]

    db_client = request.state.db
    find_ = {}
    filter_ = {"_id": 1, "name": 1, "type": 1} 
    # lấy all document langguage dc truyền vào từ request
    posts = await db_client.find_many(find_, f'lang_{language}', filter_=None)

    # lấy list name tất cả ngôn ngữ đẫ được tạo từ colection db str="lang"
    name = await get_all_language(request, db_client, "lang")
    # print(language)
    check=0
    # check xem ngôn ngữ trong list được tạo hay chưa
    for check_name in name:
        if f'lang_{language}' in  check_name:
            check+=1
    if check==1:
        print("true")
        
        context = {
            "request": request,
            "data": data,
            "posts": posts,
            "lang": language,
        }

        print(f"total: {time.time() - t0} - data: {data}")
        return templates.TemplateResponse("show_list_page.html", context)
    # chưa được tạo thì copy ra từ lang_en
    else:
        posts_copy = await db_client.find_many(find_, f'lang_en', filter_=None)
        insert_data = []
        for document in posts_copy:
            document.pop('_id')
            document.update({'lang_status': 'False'})
            if document["name"]=="home":
                document["content"]["language"].update({'tran': f'{language}'})
            # document.update('lang_status': False)
            insert_data.append(document)

        ins= await db_client.insert_many(insert_data, f'lang_{language}')
        posts = await db_client.find_many(find_, f'lang_{language}', filter_=None)
        context = {
            "request": request,
            "data": data,
            "posts": posts,
            "lang": language,
        }
        print(f"total: {time.time() - t0} - data: {data}")
        return templates.TemplateResponse("show_list_page.html", context)
 

@authenticate
async def create(request):
    t0 = time.time()
    data = {}

    language=request.path_params["lang"]
    name_page=request.path_params["name"]

    db_client = request.state.db
    find_ = {"name":name_page}

    # lấy list name tất cả ngôn ngữ đẫ được tạo từ colection db str="lang"
    name = await get_all_language(request, db_client, "lang")

    check=0
    # check xem ngôn ngữ trong list được tạo hay chưa
    for check_name in name:
        if f'lang_{language}' in  check_name:
            check+=1
    # print (check)
    if check==1:
        # print("true")
        find_ = {"name":name_page}
        posts = await db_client.find_one(find_, f'lang_{language}', filter_=None)

        #update template_post
        if posts["type"] == "template_post":
            if request.method == "POST":
                for key in posts:
                    if "tran_" in key or "content" in key:
                        form_data = await request.form()
                        name = form_data[f'{key}']
                        posts[f"{key}"].update({'tran': f'{name.strip()}'})
                
                # cập nhật trạng thái đẫ chỉnh sửa hay chưa get từ form option
                name2 = form_data["status"]
                # print(name2)
                if name2=="True":
                    posts.update({"lang_status":"True"})
                else:
                    posts.update({"lang_status":"False"})

        #update template_page
        elif posts["type"] == "template_page":
        # get key và value từ form edit và cập nhật theo các key
            if request.method == "POST":
                for key in posts["content"]:
                # print(key)
                    form_data = await request.form()
                    name = form_data[f'{key}']
                    posts["content"][f"{key}"].update(  {'tran': f'{name.strip()}'})
                
                # cập nhật trạng thái đẫ chỉnh sửa hay chưa get từ form option
                name2 = form_data["status"]
                # print(name2)
                if name2=="True":
                    posts.update({"lang_status":"True"})
                else:
                    posts.update({"lang_status":"False"})
                # submit all

        #update template_menu
        elif posts["type"] == "template_menu":
            if request.method == "POST":
                for key in posts["content"]:
                    # if "tran_" in key or "content" in key:
                    form_data = await request.form()
                    # print(key)
                    url = form_data[f"{key}_url"]
                    # print(url)
                    title = form_data[f"{key}_title"]
                    # print (title)
                    posts["content"][f"{key}"]["url"].update({'tran': f'{url.strip()}'})
                    posts["content"][f"{key}"]["title"].update({'tran': f'{title.strip()}'})
                
                # cập nhật trạng thái đẫ chỉnh sửa hay chưa get từ form option
                name2 = form_data["status"]
                # print(name2)
                if name2=="True":
                    posts.update({"lang_status":"True"})
                else:
                    posts.update({"lang_status":"False"})

        # update data vừa edit vào db
        id_ = (posts["_id"])
        up= await db_client.update_one(f"{id_}", posts, f"lang_{language}")

        
            # posts = Markup.escape(posts.)
        context = {
            "request": request,
            "data": data,
            "posts": posts,
            "lang": language,
            "name": name_page
        }

        print(f"total: {time.time() - t0} - data: {data}")
        if posts["type"] == "template_post":
            return templates.TemplateResponse("template_post.html", context)
        elif posts["type"] == "template_page":
            return templates.TemplateResponse("template_page.html", context)
        elif posts["type"] == "template_menu":
            return templates.TemplateResponse("template_menu.html", context)

    # chưa được tạo thì copy ra từ lang_en
    else:
        posts_copy = await db_client.find_many(find_, f'lang_en', filter_=None)
        insert_data = []
        for document in posts_copy:
            document.pop('_id')
            document.update({'lang_status': 'False'})
            insert_data.append(document)
        ins= await db_client.insert_many(insert_data, f'lang_{language}')
        posts = await db_client.find_many(find_, f'lang_{language}', filter_=None)
        context = {
            "request": request,
            "data": data,
            "posts": posts,
            "lang": language,
            "name": name_page
        }

        print(f"total: {time.time() - t0} - data: {data}")
        return templates.TemplateResponse("lang_edit.html", context)

