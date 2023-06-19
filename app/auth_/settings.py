SESSION_SECRET_KEY = '2jjggsj00wa45asdejlkj'
SESSION_MAX_AGE = 60 * 60 * 24 * 7
JWT_SECRET_KEY = '4534HN&*j12h0asdejlkj'
JWT_ALGORITHM = 'HS256'
JWT_MAX_AGE = 60 * 60 * 24 * 3
JWT_MAX_AGE_REMEMBER_ME = 60 * 60 * 24 * 47
DEBUG = True

# config database
DB = {
    "DB_HOST": "mongodb://adminmg:tM5Jngh9EbKu@5.161.176.184:27018/admin",
    "DB_NAME": "pinterest",
    "COL_DATA": "data",
    # "DB_HOST": "mongodb://host.docker.internal:3000/admin",
    # "DB_NAME": "starlette_test",
    "COL_USERS": "users",
    "COL_ROUTES": "routes",
    "COL_GROUPS": "groups"
}
USERS = [
    {
        "username": "admin", 
        "password": "vanthe",
        "groups": ["dev"]
    }
]

# Noti
telegram_head = "[AntC Analytics]"

# website setting
SITE_NAME = "Admin"
THEME = "sneat"