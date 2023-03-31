import aiohttp
import json
import requests
from urllib import parse
from yarl import URL

def get_url(url, params):
    url = url + '?' + parse.urlencode(params)
    return URL(url, encoded = True)

def translate_sync(url, q, s, d):
    params={"q":q,"source":s,"target":d,"format":"text"}
    return json.loads(requests.post(get_url(url + "/translate", params)).content.decode())

async def translate_async(url, q, s, d):
    async with aiohttp.ClientSession() as session:
        params={"q":q,"source":s,"target":d,"format":"text"}
        async with session.post(get_url(url + "/translate", params)) as resp: # URL canonization fails for libretranslate for feb 2023
            return json.loads(await resp.text())
