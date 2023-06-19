from starlette.routing import Mount, Route
from auth_.routes import routes as auth_routes
from auth_.middlewares import middleware as admin_middleware
from auth_.app import app as admin_app
import views
import settings
from resources import static

routes = [
    Mount(
        '/admin',
        app=admin_app
    ),

    Route("/", views.homepage, methods=["GET", "POST"]),


    Route("/{language}/{menu}", views.show_menu, methods=["GET"]),
    Route("/{language}/", views.homepage, methods=["GET", "POST"]),
    Route("/en/pin_get", views.pin_get, methods=["POST"]),
    Mount('/assets', static, name='static'),    
    Route("/en/en/en/admin", views.main, methods=["GET"]),
    Route("/sitemap.xml", views.sitemap, methods=["GET"]),
    # Route("/", views.homepage, methods=["GET", "POST"]),
    Route("/by_product", views.by_product, methods=["GET", "POST"]),
    Mount('/assets', static, name='static'),
    
    
    
    
]