from starlette.applications import Starlette
from auth_.routes import routes
from auth_.middlewares import middleware


app = Starlette(
    routes=routes,
    middleware=middleware,
)
