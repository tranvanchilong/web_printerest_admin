from settings import DB, SESSION_SECRET_KEY, SESSION_MAX_AGE, USERS
from db import MongoAsyncPipeline
import asyncio
from resources import hash_password, b_log

logger = b_log("db_create")


async def create_database():
    MONGO_URI = DB['DB_HOST']
    MONGODB_DB = DB['DB_NAME']
    db_client = MongoAsyncPipeline(MONGO_URI, MONGODB_DB)
    await db_client.check_connect()


    # Create basic routes
    routes = [
        "/",
        "/auth/delete_route",
        "/auth/edit_route",
        "/auth/add_route",
        "/auth/manage_routes",

        "/auth/delete_group",
        "/auth/edit_group",
        "/auth/add_group",
        "/auth/manage_groups",
        
        "/auth/delete_user",
        "/auth/edit_user",
        "/auth/add_user",
        "/auth/manage_users",

        "/auth/register",
        "/auth/logout",
        "/auth/login",
        "/auth/manage",
    ]
    insert_routes = [
        {"route": route} for route in routes
    ]
    route_create_index = await db_client.create_index(collection_="routes", index_=[("route", 1)], name="idx_route", unique=True, background=True)
    route_insert = await db_client.insert_many(documents_=insert_routes, collection_="routes")
    
    logger.info(f"Group - route_create_index: {route_create_index} - route_insert: {route_insert}")


    # Create basic groups
    groups = [
        {
            "group_name": "dev",
            "routes": [
                "/",
                "/auth/delete_route",
                "/auth/edit_route",
                "/auth/add_route",
                "/auth/manage_routes",
                "/auth/delete_group",
                "/auth/edit_group",
                "/auth/add_group",
                "/auth/manage_groups",
                "/auth/delete_user",
                "/auth/edit_user",
                "/auth/add_user",
                "/auth/manage_users",
                "/auth/register",
                "/auth/manage"
            ]
        },
        {
            "group_name": "admin",
            "routes": [
                "/",
                "/auth/delete_user",
                "/auth/edit_user",
                "/auth/add_user",
                "/auth/manage_users",
                "/auth/logout",
                "/auth/login",
                "/auth/manage"
            ]
        },
        {
            "group_name": "mod",
            "routes": [
                "/",
                "/auth/delete_user",
                "/auth/edit_user",
                "/auth/add_user",
                "/auth/manage_users",
                "/auth/logout",
                "/auth/login"
            ]
        },
    ]
    group_create_index = await db_client.create_index(collection_="groups", index_=[("group_name", 1)], name="idx_group_name", unique=True, background=True)
    group_insert = await db_client.insert_many(documents_=groups, collection_="groups")

    logger.info(f"Route - group_create_index: {group_create_index} - group_insert: {group_insert}")

    # Create basic users
    user_create_index = await db_client.create_index(collection_="users", index_=[("username", 1)], name="idx_username", unique=True, background=True)
    for user in USERS:
        user.update({
            "password": hash_password(user['password'])
        })
    user_insert = await db_client.insert_many(documents_=USERS, collection_="users")
    
    logger.info(f"User - user_create_index: {user_create_index} - user_insert: {user_insert}")



asyncio.run(create_database())