import requests

from wauo import WauoSpider
import json
import re

def jsonp2json(jsonp: str):
    """jsonp转换为json"""
    data: dict = json.loads(re.match(".*?({.*}).*", jsonp, re.S).group(1))
    return data


def parse(jsonData: dict):
    comments = jsonData["data"]["comments"]
    for c in comments:
        nickname = c["tbNick"]
        content = c["content"]
        commentId = c["commentId"]
        print("{}：{}（{}）".format(nickname, content, commentId))


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "_m_h5_tk": "6099357e6e2c3877fbd091fe693c1975_1735617965048",
    "_m_h5_tk_enc": "9d2a3bc505d8b4ac4ce3c774ef21d1a8",
}
url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "34675810",
    "t": "1735610185133",
    "sign": "447fc197f211e7c8b3596611985933c9",
    "timeout": "10000",
    "data": "{\"topic\":\"8a31cf96-9920-49cb-a9c7-b2695a8994f6\",\"limit\":20,\"tab\":2,\"order\":\"asc\",\"paginationContext\":\"{\\\"commentId\\\":501744532537,\\\"refreshTime\\\":1735610184235,\\\"timestamp\\\":1735610049000}\"}"
}
res = requests.get(url, headers=headers, cookies=cookies, params=params)
print(res.text)
jsonData = jsonp2json(res.text)
parse(jsonData)
# from pprint import pprint as print
# print(jsonData,width=20)

data = {
    "topic": "8a31cf96-9920-49cb-a9c7-b2695a8994f6",
    "limit": 20,
    "tab": 2,
    "order": "asc",
    "paginationContext": "{\"commentId\":501744532537,\"refreshTime\":1735610184235,\"timestamp\":1735610049000}"
}

r = json.dumps(data)
print(r)