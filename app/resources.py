from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
import jwt
import bcrypt
import settings
import urllib.parse
import re
import httpx
import arrow
import random
import traceback
import os
import logging
from logging.handlers import RotatingFileHandler
import settings
import asyncio

static = StaticFiles(directory=f'./themes/{settings.THEME}/static')
templates = Jinja2Templates(
    directory=f'./themes/{settings.THEME}/templates',
    autoescape=False, 
    auto_reload=True, 
    # enable_async=True,
)
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
# Async request
#
class async_rq:
    '''
    Class request gộp chung khởi tạo session, rate limit, timeout
    '''
    def __init__ (self, time_out=30):
        # Khởi tạo rate limit
        self.time_out = time_out
    async def async_request_all(self, url, type, payload=None, proxy=None, headers=None, method="GET"):
        t0 = time.time()
        if proxy != None: http_proxy = {"http://": proxy, "https://": proxy}
        else: http_proxy = None

        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        if headers == None: headers = {
            'user-agent': ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
            'Accept-Language': 'en-US,en;q=0.5', 
            'Accept-Encoding': 'gzip, deflate'
        }
        else: headers.update({'user-agent': ua})

        try:
            async with httpx.AsyncClient(http2=True) as session:
                if method == "GET":
                    async with session.get(url, headers=headers, proxies=http_proxy, timeout=self.timeout) as response:
                        if type == "JSON": html = await response.json()
                        else: html = await response.text
                elif method == "POST": 
                    if type == "JSON":
                        async with session.post(url, headers=headers, json=payload, proxies=http_proxy, timeout=self.timeout) as response:
                            html = await response.json()
                    else: 
                        async with session.post(url, headers=headers, data=payload, proxies=http_proxy, timeout=self.timeout) as response:
                            html = await response.text
            
            status= response.status_code
            headers = html['headers']
            request_info = response.request

        except:
            status = str(traceback.format_exc())
            headers = request_info = html = ''

        return {
            'url': url,
            'status': status,
            "headers": headers,
            "request_info": request_info,
            "html": html,
            "proxy": proxy,
            "request_time": f"{time.time() - t0:.2f}"
        }



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
            'route' : '/by_product',
            'name' : 'Product created & sold',
        },
        {
            'route' : '/by_item',
            'name' : 'By Item',
        },
        {
            'route' : '/by_revenue',
            'name' : 'By Revenue',
        },
        {
            'route' : '/customily_unique_domain',
            'name' : 'Customily Domain',
        },
        {
            'route' : '/export_order',
            'name' : 'Export Order',
        },
        {
            'route' : '/fulfill',
            'name' : 'Fulfill Order',
        },
    ]
static = StaticFiles(directory=f'./themes/{settings.THEME}/static')
templates = Jinja2Templates(
    # directory='./templates',
    # directory='./themes/skeleton/templates',
    directory=f'./themes/{settings.THEME}/templates',
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

async def wait_first_task(tasks):
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for x in done:
        result = x.result()
        if result:
            for task in pending:
                task.cancel()
            await asyncio.wait(pending)
            return result


templates.env.globals['CustomURLProcessor'] = CustomURLProcessor
templates.env.globals['encode_url'] = encode_url
templates.env.globals['jwt_decode'] = jwt_decode
templates.env.globals['j2_route_perm'] = jinja_check_route_permission
templates.env.globals['j2_group_perm'] = jinja_check_group_permission
templates.env.globals['site_name'] = site_name
templates.env.globals['jinja_list_routes'] = jinja_list_routes