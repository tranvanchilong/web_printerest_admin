from starlette.routing import Mount, Route
from . import views, views_edit
from starlette.staticfiles import StaticFiles
import settings
from .T_modules import language_api

routes = [
    # Route("/", endpoint=views.redirect_main, methods=["GET"]),
    Route("/", endpoint=views.admin_page, methods=["GET"]),
    Route("/test_authen", endpoint=views.test_authen_page, methods=["GET"]),
    Route("/manage", endpoint=views.redirect_main, methods=["GET"]),

    Route("/login", endpoint=views.login_page, methods=["GET", "POST"]),
    Route("/logout", endpoint=views.logout_page, methods=["GET", "POST"]),
    Route("/register", endpoint=views.register_page, methods=["GET", "POST"]),
    Route("/manage_users", endpoint=views.manage_users_page, methods=["GET"]),
    Route("/add_user", endpoint=views.add_user_page, methods=["GET", "POST"]),
    Route("/edit_user", endpoint=views.edit_user_page, methods=["GET", "POST"]),
    Route("/delete_user", endpoint=views.delete_user_page, methods=["GET"]),

    Route("/manage_groups", endpoint=views.manage_groups_page, methods=["GET", "POST"]),
    Route("/add_group", endpoint=views.add_group_page, methods=["GET", "POST"]),
    Route("/edit_group", endpoint=views.edit_group_page, methods=["GET", "POST"]),
    Route("/delete_group", endpoint=views.delete_group_page, methods=["GET", "POST"]),
    
    Route("/manage_routes", endpoint=views.manage_routes_page, methods=["GET", "POST"]),
    Route("/add_route", endpoint=views.add_route_page, methods=["GET", "POST"]),
    Route("/edit_route", endpoint=views.edit_route_page, methods=["GET", "POST"]),
    Route("/delete_route", endpoint=views.delete_route_page, methods=["GET", "POST"]),


    Route("/homepage_edit", endpoint=views_edit.homepage_edit, methods=["GET", "POST"]),
    # Route("/homepage_edit", endpoint=views_edit.lang_edit, methods=["GET", "POST"]),
    # Route("/homepage_edit/create_{language}", endpoint=views_edit.lang_edit, methods=["GET", "POST"]),
    Route("/homepage_edit/manage_{language}/", endpoint=views_edit.show_list_page, methods=["GET", "POST"]),
    Route("/homepage_edit/{name}/create_{lang}/", endpoint=views_edit.create, methods=["GET", "POST"]),
    # Route("/en/en/en/en/main/", endpoint=views_edit.main, methods=["GET", "POST"]),
    
    
    # thông (test nên sẽ ko để methods)

    Route("/language_api/create_language/{lang}", language_api.creat_newlanguage, methods=["GET", "POST"]),
    Route("/language_api/get_all", language_api.get_all_language, methods=["GET", "POST"]),
    Route("/language_api/get_lang/{lang}/", language_api.find_language, methods=["GET", "POST"]),

    Route("/language_api/lang_id/{collection_name}_{_id}", language_api.find_data_in_lang, methods=["GET", "POST"]),
    Route("/language_api/lang_status/{collection_name}_{_id}", language_api.fix_status_id_in_collection, methods=["GET", "POST"]),
    Route("/language_api/lang_allstatus/{lang}", language_api.check_all_status_language, methods=["GET", "POST"]),  
    Route("/language_api/lang_id/{collection_name}_{_id}", language_api.find_data_in_lang, methods=["GET", "POST"]),
    # Route("/language_api/lang_status/{collection_name}_{_id}", language_api.fix_status_id_in_collection, methods=["GET", "POST"]),
    # Route("/language_api/lang_allstatus/{lang}", language_api.check_all_status_language, methods=["GET", "POST"]),  



    # end thông
    
    # Route("/homepage_edit", endpoint=views.homepage_edit, methods=["GET"]),

    Mount('/assets', StaticFiles(directory=f'./auth_/themes/sneat_admin/assets'), name='auth_static'),
]