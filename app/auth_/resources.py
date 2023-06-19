from starlette.templating import Jinja2Templates
from starlette.requests import Request
import jwt
import bcrypt
import urllib.parse
import arrow
import os
import logging
from logging.handlers import RotatingFileHandler
import settings


# Log ----------------
def b_log(log_name, stream = True):
    def tz_converter(*args):
        return arrow.utcnow().to('+07:00').timetuple()
        return datetime.now(tz).timetuple()
        
    os.makedirs('./logs/') if not os.path.exists('./logs/') else True
    logger = logging.getLogger(log_name)
    logging.Formatter.converter = tz_converter

    hnd_all = RotatingFileHandler('./logs/' + log_name + ".log", maxBytes=10000000, backupCount=5, encoding='utf-8')
    # hnd_all.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
    hnd_all.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(filename)s:%(lineno)d]', datefmt='%Y%m%d %H:%M:%S'))
    hnd_all.setLevel(logging.INFO)
    logger.addHandler(hnd_all)

    if stream == True:
        hnd_stream = logging.StreamHandler()
        # hnd_stream.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
        # hnd_stream.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(filename)s:%(lineno)d]', datefmt='%Y%m%d %H:%M:%S'))
        hnd_stream.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(filename)s:%(lineno)d]', datefmt='%H:%M:%S'))
        hnd_stream.setLevel(logging.INFO)
        logger.addHandler(hnd_stream)

    logger.setLevel(logging.DEBUG)

    return logger


#
# Encryption
#
def jwt_encode(data):
    encoded_jwt = jwt.encode(data, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
def jwt_decode(encoded_jwt):
    try:
        data = jwt.decode(encoded_jwt, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return data
    except jwt.ExpiredSignatureError: # token hết hạn sẽ tự động có exception này
        return False
    except: # có thể cần thêm log cho chuẩn chỉnh
        return False
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


#
# Common functions
#
def flat_list(l):
    return [item for sublist in l for item in sublist]
def site_name():
    return settings.SITE_NAME
def show_session(request):
    session = request.session
    print(f"show session: {session}")
def encode_url(url):
    return urllib.parse.quote_plus(url)
def decode_url(url):
    return urllib.parse.unquote(url)


#
# Jinja
#
def jinja_check_route_permission(route, session_data):
    if session_data == False:
        return False
    if 'dev' in session_data['groups']:
        return True
    user_routes = session_data['user_routes']
    if not str(route) in user_routes:
        return False
    else:
        return True
def jinja_check_group_permission(group_data, session_data):
    group_split = group_data.split(",")
    if session_data == False:
        return False
    if 'dev' in session_data['groups']:
        return True
    groups = session_data['groups']
    if not any([str(group) in groups for group in group_split]):
        return False
    else:
        return True
def jinja_list_routes():
    return [
        {
            'route' : '/admin/homepage_edit',
            'name' : 'Home Page Edit',
        },
    ]
templates = Jinja2Templates(
    # directory='./templates',
    # directory='./themes/skeleton/templates',
    directory=f'./auth_/themes/sneat_admin/templates',
    autoescape=False, 
    auto_reload=True, 
    # enable_async=True,
)

class CustomURLProcessor:
    def __init__(self):  
        self.path = "" 
        self.request = None

    def url_for(self, request: Request, name: str, **params: str):
        self.path = request.url_for(name, **params)
        self.request = request
        return self
    
    def include_query_params(self, **params: str):
        parsed = list(urllib.parse.urlparse(self.path))
        parsed[4] = urllib.parse.urlencode(params)
        return urllib.parse.urlunparse(parsed)

templates.env.globals['CustomURLProcessor'] = CustomURLProcessor
templates.env.globals['encode_url'] = encode_url
templates.env.globals['jwt_decode'] = jwt_decode
templates.env.globals['j2_route_perm'] = jinja_check_route_permission
templates.env.globals['j2_group_perm'] = jinja_check_group_permission
templates.env.globals['site_name'] = site_name
templates.env.globals['jinja_list_routes'] = jinja_list_routes