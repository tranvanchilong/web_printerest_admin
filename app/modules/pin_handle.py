from resources import async_rq
import httpx
from parsel import Selector
import json
import time
import traceback
import time

async def pin_handle_data(url):
    t0 = time.time()
    print(f"url: {url}")
    
    # Request
    async with httpx.AsyncClient(http2=True) as client:
        post_request = await client.post('https://www.expertsphp.com/download.php', data={'url': url})
    
    if post_request.status_code == 200:
        result = True
    else:
        result = False
    
    # parse
    selector = Selector(text=post_request.text)
    # video_url = selector.css('video').get()
    video_url = selector.css('video').attrib['src']
    
    for download in selector.css('table tr td a'):
        url = download.attrib['href']
        if '.mp4' not in url:
            image = url
    
    print(f"pin_handle_data time: {time.time() - t0}")
    return {
        'result': result,
        'video': video_url,
        'image': image,
        "video_list": []
    }
async def pin_handle_data_2(url):
    try:
        t0 = time.time()
        print(f"url: {url}")
        
        # Get id https://www.pinterest.com/pin/612419249362161142/?mt=login
        url_split = url.split('/pin/')[1]
        if "/" in url_split:
            id_ = url_split.split("/")[0]
        else:
            id_ = url_split
        # Request
        headers = None
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        if headers == None: headers = {
            'user-agent': ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
            'Accept-Language': 'en-US,en;q=0.5', 
            'Accept-Encoding': 'gzip, deflate'
        }
        else: headers.update({'user-agent': ua})
        async with httpx.AsyncClient(http2=True) as client:
            # print (url) #ok
            response = await client.get(url, headers=headers, timeout=10)
        print (url)
        if response.status_code == 200:
            result = True
        else:
            result = False
        
        # parse
        selector = Selector(text=response.text)
        
        # get list video
        try:
            data = selector.css("script#__PWS_DATA__::text").get()
            data = json.loads(data)
            # video_data = data['props']['initialReduxState']['pins'][id_]['videos']['video_list']
            video_data = data['props']['initialReduxState']['pins'][id_]['story_pin_data']['pages'][0]['blocks'][0]['video']['video_list']
            print(f"video_data: {video_data}")
            video_list = []
            # print ("url")
            for video in video_data:
                url = video_data[video]['url']
                if ".mp4" in url:
                    async with httpx.AsyncClient(http2=True) as client:
                        
                        response = await client.head(url, headers=headers, timeout=10)
                        # print(f"response head: {response.headers}")
                        file_size = round(float(int(response.headers['content-length']) / 1024 / 1024), 2)
                        print(f"size: {file_size} mb")
                        video_list.append({
                            'url': url,
                            "size": file_size
                        })
            
            dict_to_sort = {item["size"]: item for item in video_list}
            dict_to_sort = dict(reversed(sorted(dict_to_sort.items())))
            new_video_list = [dict_to_sort[key] for key in dict_to_sort]
            print(f"new_video_list: {new_video_list}")
        except:
            new_video_list = []
            # print (url)

        
        
        data = selector.css("script[data-test-id='leaf-snippet']::text").get()
        data = json.loads(data)
        image = data['image']
        # print(type(data['image']))
        data = selector.css("script[data-test-id='video-snippet']::text").get()
        data = json.loads(data)
        video_url = data['contentUrl']
        
        
        print(f"pin_handle_data_2 time: {time.time() - t0}")
        # print (video_url)
            
        return {
            'result': result,
            'video': video_url,
            'image': image,
            "video_list": new_video_list
        }
    except:
        time.sleep(10)
        return{
            'data': False,
            'result': traceback.format_exc(),
            'video': "",
            'image': "",
            "video_list": ""
        }
async def test(pdb_id):
    # API Endpoint
    URL = "https://klifs.net/api/structures_pdb_list"
    
    # PDB we would like to query for
    PARAMS = {'pdb-codes': pdb_id}

    # Send the GET request to the API and retrieve any returned data
    res = httpx.get(url = URL, params = PARAMS)
    data = res.json()

    # If an error occured, return the error
    if res.status_code == 400:
        return data[1], 400
        
    # Return the first set of PDB characteristics
    return data[0]