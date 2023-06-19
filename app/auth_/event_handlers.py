from starlette.applications import Starlette
from starlette.responses import RedirectResponse

async def unauthorized(request, exc):
    return RedirectResponse(url='/auth/login_page')

exception_handlers = {
    401: unauthorized,
    403: unauthorized,
}
