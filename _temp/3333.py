import json
import re
import time
import requests
import hashlib
from pygments import highlight, lexers, formatters


def get_sign(string):
    return hashlib.md5(string.encode()).hexdigest()


def req(sign,now,data):
    cookies = {
        #添加你自己的cookies
    }

    headers = {
        'authority': 'h5api.m.tmall.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'referer': 'https://detail.tmall.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    params = {
        'jsv': '2.7.0',
        'appKey': '12574478',
        't': now,
        'sign': sign,
        'api': 'mtop.alibaba.review.list.for.new.pc.detail',
        'v': '1.0',
        'isSec': '0',
        'ecode': '0',
        'timeout': '10000',
        'ttid': '2022@taobao_litepc_9.17.0',
        'AntiFlood': 'true',
        'AntiCreep': 'true',
        'preventFallback': 'true',
        'type': 'jsonp',
        'dataType': 'jsonp',
        'callback': 'mtopjsonp3',
        'data': data,
    }

    response = requests.get(
        'https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    json_str = re.findall(r'mtopjsonp3\((.*?)\)',response.text)
    content = json.loads(json_str[0])
    formatted_json = json.dumps(content, indent = 4, ensure_ascii = False, sort_keys = True)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)

def get_time_13():
    return int(time.time()*1000)

if __name__ == "__main__":
    token = '换成你自己的token'
    pageNum = 1 #1-6页能爬取
    data = f'{"itemId":"677739475107","bizCode":"ali.china.tmall","channel":"pc_detail","pageSize":20,"pageNum":{pageNum}}'
    l = get_time_13()
    s = '12574478'
    p1 = token + "&" + str(l) + "&" + s + "&" + data
    print(p1)
    sign = get_sign(p1)
    req(sign=sign,now=l,data=data)