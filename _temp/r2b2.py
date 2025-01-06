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
    "_m_h5_tk": "e200931c55019d4b2a9257caf78ce355_1735624562117",
    "_m_h5_tk_enc": "88da63ba111130a180a4663f8777ec04",
}
url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "34675810",
    "t": "1735615360775",
    "sign": "1a7625b23b3eb61e60272711e023a8f0",
    "timeout": "10000",
    "data": '{\"topic\":\"f67b36e8-ec3a-4347-8f89-91b7ce2ec3c5\",\"limit\":20,\"tab\":2,\"order\":\"asc\",\"paginationContext\":\"{\\\"commentId\\\":501947807204,\\\"refreshTime\\\":1735615360150,\\\"timestamp\\\":1735615113000}\"}'

}
res = requests.get(url, headers=headers, cookies=cookies, params=params)
print(res.text)
jsonData = jsonp2json(res.text)
parse(jsonData)
# from pprint import pprint as print
# print(jsonData,width=20)
