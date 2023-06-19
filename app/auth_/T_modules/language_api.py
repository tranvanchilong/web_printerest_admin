from starlette.responses import PlainTextResponse, Response, JSONResponse, StreamingResponse
from resources import templates, jwt_decode
from auth_.users import authenticate, get_user_session, get_user
from starlette.background import BackgroundTask
import arrow
import time
import json
import traceback
from resources import templates
# from db import MongoAsyncPipeline
from settings import DB 
import asyncio
from bson import ObjectId
# import requests
# import aiohttp

# Thông

# hàm trả về tất cả những ngôn ngữ đang có trên db
async def get_all_language(request):

    list_language = []
    db_client_x = request.state.db
    collection_names = await db_client_x.select_all_collections()
    for lang_a in collection_names:
        if "lang_" in  lang_a:
            add_b = lang_a.split("_")[1]
            list_language.append(add_b)
    await send_to_telegram(f"test {list_language} ")
    return JSONResponse(list_language)
# async def find_language(request):


# hàm tạo thêm nngoon ngữ nếu nó chưa tồn tại
async def creat_newlanguage(request):
    try:
        db_client_x = request.state.db
        lang_input = request.path_params["lang"]
        if "lang_" not in  lang_input :
            lang_input  ="lang_" + str(lang_input )
        collection_names = await db_client_x.find_all_collections(name_col = lang_input)
        if collection_names != True:
            set_dict_lang =  await db_client_x.find_many(item = {},collection_ = DB["DB_col_set"])
            for doc in set_dict_lang:
                doc.pop("_id")
                if 'lang_status' in doc:
                    doc.update({"lang_status": False})
                await db_client_x.insert_one(doc, collection_names)

            return JSONResponse(f"{lang_input}Tạo ngôn ngữ thành công")
        else:

            return JSONResponse(f"{lang_input} đã tồn tại bạn chỉ có thể update")
            # return JSONResponse(f"collection {collection_names} đã tồn tại")
    except: 
        print(f"error {traceback.format_exc()} ")
        return JSONResponse("lỗi không nhận được dữ liệu")
    
# tìm ngôn ngữ xem có tồn tại hay ko,nếu tồn tại thì trả về cơ số dict(bắt buộc mỗi dict phải có name,type,id)
async def find_language(request):
    # if : thêm method == post và nếu method == post thì update   (xóa id để tránh lỗi)  

    try:
        db_client_x = request.state.db
        lang_input = request.path_params["lang"]
        if "lang_" not in  lang_input :
            lang_input  ="lang_" + str(lang_input)
        check_lang = await db_client_x.find_all_collections(name_col = lang_input)
        if check_lang == True:
            set_dict_lang =  await db_client_x.find_many(item = {},collection_ = lang_input)
            
            if set_dict_lang != None: 
                mum = []
                for doc in set_dict_lang:
                    if 'lang_status' in doc:
                        # if doc["lang_status"] == True:
                        id = str(doc["_id"])
                        mum.append({"id": id , "name": doc["name"], "type": doc["type"], "lang_status": doc["lang_status"]})
                return JSONResponse(mum)

            else:
                return JSONResponse({"status": "không tìm thấy ngôn ngữ/ngôn ngữ chưa được tạo"})
        else:
            return JSONResponse({"status": "không tìm thấy ngôn ngữ/ngôn ngữ chưa được tạo"})
    except :
        print(f"creat_newlanguage {traceback.format_exc()} ")
        await send_to_telegram(f"creat_newlanguage {traceback.format_exc()} ")
        return JSONResponse({"status": "error"})


# hàm tìm kiếm dựa trên id và name lang
async def find_data_in_lang(request):
    try:
        if request.method == "GET":
            db_client_x = request.state.db
            lang_input = request.path_params["collection_name"]
            lang_id = request.path_params["_id"]
            if "lang_" not in  lang_input :
                lang_input  ="lang_" + str(lang_input)
            check = await db_client_x.find_colection_id(lang_input, lang_id)
            if check != None:
                check.pop("_id")
                return JSONResponse(check)
            else:
                message = f"ngôn ngữ {lang_input} với id {lang_id} không được tìm thấy"
                return JSONResponse(message)
        
        
        elif request.method == "POST":
            # form_data = await request.form()
            # form_dict = {key: value for key, value in form_data.items()}

            form_dict = await request.json()
            db_client_x = request.state.db
            lang_input = request.path_params["collection_name"]
            if "lang_" not in  lang_input :
                lang_input  ="lang_" + str(lang_input)
            lang_id = request.path_params["_id"]
            check = await db_client_x.update_one(lang_id, form_dict, lang_input)
            return JSONResponse(form_dict)
    except: 
        # await send_to_telegram(f"link_res {traceback.format_exc()} await func")
        print(f"error_link {traceback.format_exc()}")
        return JSONResponse("lỗi không thể tìm thấy kết quả phù hợp")



# dựa trên collection và id truyền vào ta sẽ thay đổi status của đối tượng được chỉ định thành true/false
async def fix_status_id_in_collection(request):
    try:
        db_client_x = request.state.db
        lang_input = request.path_params["collection_name"]
        lang_id = request.path_params["_id"] 
        if "lang_" not in  lang_input :
            lang_input  ="lang_" + str(lang_input)

        if request.method == "GET":
            check = await db_client_x.find_colection_id(lang_input, lang_id)
            if check != None:
                form_dict = {}
                if check["lang_status"] == True:
                    form_dict = {"lang_status": False }

                elif check["lang_status"] == False:
                    form_dict = {"lang_status": True }

                check = await db_client_x.update_one(lang_id, form_dict, lang_input)
                return JSONResponse(f"đã update trạng thái thành công trạng thái hiện tại là {form_dict}")
            else:
                message = f"ngôn ngữ {lang_input} với id {lang_id} không được tìm thấy"
                return JSONResponse(message)
        elif request.method == "POST":
            set_dict_lang =  await db_client_x.find_many(item = {},collection_ =lang_input)
            for doc in set_dict_lang:
                if 'lang_status' in doc:
                    if doc["lang_status"] == False:
                        return JSONResponse(False)
            return JSONResponse(True)
    except :
        print(f"fix_status_id {traceback.format_exc()} ")
        await send_to_telegram(f"creat_newlanguage {traceback.format_exc()} ")
        return traceback.format_exc()

async def check_status_lang(db_client_x, lang_input):
    try:
        set_dict_lang =  await db_client_x.find_many(item = {},collection_ =lang_input)
        for doc in set_dict_lang:
            if 'lang_status' in doc:
                if doc["lang_status"] == False:
                    return JSONResponse(False)
    except :
        print(f"fix_status_id {traceback.format_exc()} ")
        await send_to_telegram(f"check_status_lang {traceback.format_exc()} ")
        return traceback.format_exc()


# hàm quản lí status
async def check_all_status_language(request):
    db_client_x = request.state.db
    lang_input = request.path_params["lang"]
    if "lang_" not in  lang_input :
        lang_input  ="lang_" + str(lang_input )
    collection_names = await db_client_x.find_all_collections(name_col = lang_input)
    if collection_names == True:
        set_dict_lang =  await db_client_x.find_many(item = {},collection_ =lang_input)
        if set_dict_lang != []:
            
            # method == "GET" hàm kiểm tra ngôn ngữ đó và trả về trạng thái của từng thành  phần trong ngôn ngữ đó (dịch hoàn thành hay chưa)
            if request.method == "GET":
                mum = []
                for doc in set_dict_lang:
                    if 'lang_status' in doc:
                        # if doc["lang_status"] == True:
                        id = str(doc["_id"])
                        mum.append({"id": id , "name": doc["name"] , "lang_status": doc["lang_status"]})
                return JSONResponse(mum)
            
            # method == "POST" gửi biến lang_status = True/False vào trong 1 ngôn ngữ nào đó và chuyển hết thành true/false
            elif request.method == "POST":
                try:
                    form_dict = await request.json()
                    task = []
                    # form_dict = {key: value for key, value in form_data.items()}
                    if "lang_status" not in form_dict:
                        return JSONResponse("bạn cần cung cấp cho tôi lang_status ")
                    print({form_dict['lang_status']})
                    for doc in set_dict_lang:
                        if 'lang_status' in doc:
                            if doc["lang_status"] != form_dict["lang_status"]:
                                form_ = {"lang_status": form_dict["lang_status"]}
                                t = db_client_x.update_one(doc["_id"], form_, lang_input)
                                task.append(t)
                    await asyncio.gather(*task)
                    return JSONResponse(f"Đã hoàn thành update ngôn ngữ {lang_input} trở về trạng thái toàn bộ đều {form_dict['lang_status']} ")
    
                except:
                    print(f"eror post {traceback.format_exc()} ")

    else:
        return JSONResponse(f"không tìm thấy: {lang_input} hãy thử lại sau")



async def send_to_telegram(message):
    message = "[language_api] - \n" + message
    apiToken = '5921163584:AAGFHM9bpHz19bELr9J4gCSViDNPy2K_2R8'
    chatID = '5787707961'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        await  send_post_request(url=apiURL,data={'chat_id': chatID, 'text': message})
    except Exception as e:
        await  send_post_request(url=apiURL, data={'chat_id': chatID, 'text': e})


# async def send_to_group_telegram(message):
#     message = "[language_api] - \n" + message
#     apiToken = '5951493280:AAGAlhQmGrG88nEqQ39uEFUxX9cB5Pi1WF8'
#     chatID = '-892437569'
#     apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
#     try:
#         requests.post(apiURL, json={'chat_id': chatID, 'text': message})
#         # print(response.text)
#     except Exception as e:
#         requests.post(apiURL, json={'chat_id': chatID, 'text': e})
#         # print(e)


# async def send_post_request(url, data):
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=data) as response:
#             return await response.json()


# # end thông