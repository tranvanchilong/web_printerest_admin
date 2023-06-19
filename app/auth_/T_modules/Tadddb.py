from db import MongoAsyncPipeline
from settings import DB , posthome,  posts2_2, posts2_3, posts2_4, posts2_5 , sknu_link, list_lang
import asyncio
import traceback

# C:\Users\Thong\Desktop\test_delete\web_printerest_admin\app\T_add_db.py
async def main():
    # C:\Users\Thong\Documents\testweb\test\t_web_tiktokdownloader\app\add_db.py
    print("xong")
    db_client = MongoAsyncPipeline(DB['DB_HOST'], DB['DB_NAME'])
    # db_client = MongoAsyncPipeline((DB["DB_HOST"],[DB["DB_NAME"]]))
    # db_client = MongoClient(DB["DB_HOST"])
    # collection_names = db_client[DB["DB_NAME"]].list_collection_names()
    # In danh sách tên collection
    # print(collection_names)
    # for name in collection_names:
    #     print(name)
# sknu_link
    # try:
    #     await db_client.insert_one(posthome, "lang_demo")
    # except:
    #     print(f"link_res {traceback.format_exc()} await func")
    # await db_client.insert_one(sknu_link, "lang_demo")
    # await db_client.insert_one(posts2_2, "lang_demo")
    # await db_client.insert_one(posts2_3, "lang_demo")
    # await db_client.insert_one(posts2_4, "lang_demo")
    # await db_client.insert_one(posts2_5, "lang_demo")
    await db_client.insert_one(list_lang, "list_lang")
    print("xong")

if __name__ == "__main__":
    asyncio.run(main())







