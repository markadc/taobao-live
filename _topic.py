import requests

from dec.calljs import gen_sign
from tools import jsonp2json

url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/?jsv=2.7.2&appKey=34675810&t=1735890542853&sign=1cf804046b8edeb4daa87919f51c176f&api=mtop.taobao.iliad.comment.query.latest&v=1.0&timeout=10000&preventFallback=true&type=jsonp&dataType=jsonp&callback=mtopjsonp26&data=%7B%22topic%22%3A%2271768acd-f0ca-4676-813a-49503916298c%22%2C%22limit%22%3A20%2C%22tab%22%3A2%2C%22order%22%3A%22asc%22%2C%22paginationContext%22%3A%22%7B%5C%22commentId%5C%22%3A502159776011%2C%5C%22refreshTime%5C%22%3A1735890543722%2C%5C%22timestamp%5C%22%3A1735859839804%7D%22%7D"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/532.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
headers = {"User-Agent": ua}
res = requests.get(url, headers=headers)
cookies = res.cookies.get_dict()
tk = cookies["_m_h5_tk"]
tk_enc = cookies["_m_h5_tk_enc"]
token = tk.split("_")[0]

headers = {
    "referer": "https://tbzb.taobao.com/live",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

cookies = {"_m_h5_tk": tk, "_m_h5_tk_enc": tk_enc,}

ts = "1736129415326"
appKey = "34675810"
data = '{"liveId":"501743316235","productType":"live","liveSource":"source_pc_live","entryLiveSource":"source_pc_live","useLiveFandom":false}'

sign = gen_sign(token, ts, appKey, data)
print(sign)
sign = "7a5c3b191c339f49cfa0a23947abace3"

url = "https://h5api.m.taobao.com/h5/mtop.tblive.live.detail.query/4.0/"
params = {
    "jsv": "2.7.2",
    "appKey": appKey,
    "t": ts,
    "sign": sign,
    "data": data
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.text)

jsonData = jsonp2json(response.text)
topic = jsonData["data"]["topic"]
print(topic)
