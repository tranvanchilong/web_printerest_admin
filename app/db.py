from motor.motor_asyncio import AsyncIOMotorClient
import random
from pymongo.errors import BulkWriteError
from bson import ObjectId
from resources import b_log
import traceback

class MongoAsyncPipeline:
    def __init__(self, MONGO_URI, MONGODB_DB):
        self.client = AsyncIOMotorClient(MONGO_URI, retryWrites=False)
        self.db = self.client[MONGODB_DB]
        self.logger = b_log('b_db')
        
    def select_db(self, db_name):
        self.db = self.client[db_name]
        

    # hàm viết thêm

    # async def create_collection(self, collection_):
    #     collection = self.db[collection_]
    #     await collection.create()
    #     await self.db.close()
    #     return collection_

    # all_text_collections là hàm giống với hàm  find_many 
    # async def all_text_collections(self, collection_):
    async def all_text_collections(self):
        # await db.list_collection_names(filter=filter)
        list_collections = await self.db.find()
        return list_collections

    # trả về danh sách tên của tất cả các collection 
    async def select_all_collections(self):
        # await db.list_collection_names(filter=filter)
        list_collections = await self.db.list_collection_names()
        return list_collections
    # kiểm tra collection có ở trong db hay ko
    async def find_all_collections(self, name_col):
        # filter = {"name": {"$regex": r"^(?!system\.)"}}
        # await db.list_collection_names(filter=filter)
        list_collections = await self.db.list_collection_names()
        if name_col not in list_collections:
            return name_col
        else:
            return True

    async def find_colection_id(self, collection, id):
        my_collection = self.db[collection]
        # Tìm một bản ghi với _id là id
        result = await my_collection.find_one({'_id': ObjectId(id)})

        # In kết quả tìm được
        return result

        


    # hàm ban đầu
    async def check_connect(self):
        try:
            await self.client.server_info()
            self.logger.info(f'Db connected')
        except Exception as e:
            self.logger.exception("connect error")

    
    async def insert_one(self, document_, collection_):
        collection_ = self.db[collection_]
        try:
            result = await collection_.insert_one(document_)
            self.logger.debug(msg=f'inserted data: {result.inserted_id}')
            return result.inserted_id
        except BulkWriteError as e:
            dup_keys = len([x for x in e.details['writeErrors'] if 'E11000 duplicate key error collection' in x['errmsg']])
            return 'Dupkey'
        except Exception as e:
            if 'E11000 duplicate key error collection' in str(e):
                return 'Dupkey'
            else:
                self.logger.exception("insert error")
                return "error"


    async def insert_many(self, documents_, collection_):
        collection_ = self.db[collection_]
        try:
            result = await collection_.insert_many(documents_, ordered=False)
            return len(result.inserted_ids)
        except BulkWriteError as e:
            dup_keys = len([x for x in e.details['writeErrors'] if 'duplicate key error' in x['errmsg']])
            return 'Dupkey', dup_keys
        except Exception as e:
            if 'E11000 duplicate key error collection' in str(e):
                return 'Dupkey', documents_
            else:
                return "error", str(traceback.format_exc())
    
    
    async def create_index(self, collection_, index_, name, unique=False, background=True):
        collection_ = self.db[collection_]
        return await collection_.create_index(index_, unique=unique, background=background, name=name)
    

    async def find_one(self, item, collection_, filter_=None):
        collection_ = self.db[collection_]
        return await collection_.find_one(item, filter_)
    
    
    async def delete(self, item, collection_):
        collection_ = self.db[collection_]
        result = await collection_.delete_many(item)
        if result.deleted_count > 0:
            return True
        else:
            return False
   
    
    async def find_many(self, item, collection_, filter_=None, limit_=0):
        collection_ = self.db[collection_]
        all_ = []
        db = collection_.find(item, filter_).limit(limit_)
        async for document in db:
            all_.append(document)
        return all_
    async def find_many_limit_sort_latest(self, item, collection_, filter_=None, limit_=0, sort_="_id"):
        collection_ = self.db[collection_]
        all_ = []
        db = collection_.find(item, filter_).limit(limit_).sort(sort_, -1)
        async for document in db:
            all_.append(document)
        return all_

    # async def find_all(self,collection_, filter_=None):
    #     collection_ = self.db[collection_]
    #     cursor = collection_.find({})
    #     for document in cursor:
    #         print(document)
        # return await collection_.find_one(item, filter_)

    async def update_one(self, _id, update_, collection_):
        collection_ = self.db[collection_]
        return await collection_.update_one({'_id': ObjectId(_id)}, {'$set': update_}, upsert=True)
    async def update_remove_one(self, _id, update_, collection_):
        collection_ = self.db[collection_]
        return await collection_.update_one({'_id': ObjectId(_id)}, {'$unset': update_}, upsert=True)

    async def select_all_collections(self):
        # await db.list_collection_names(filter=filter)
        list_collections = await self.db.list_collection_names()
        return list_collections
    

