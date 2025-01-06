import requests

from dec.calljs import gen_sign
from tools import show_barr, make_token


tk, tk_enc, token = make_token()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "_m_h5_tk": tk,
    "_m_h5_tk_enc": tk_enc,
}

ts = "1736129415326"
appKey = "34675810"
data = '{"topic":"2b95ce32-e038-4fac-85f2-9ec2fd8f49bc","limit":20,"tab":2,"order":"asc","paginationContext":"{\\"commentId\\":502642448206,\\"refreshTime\\":1736129415041,\\"timestamp\\":1736129413000}"}'

sign = gen_sign(token, ts, appKey, data)

url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": appKey,
    "t": ts,
    "sign": sign,
    "api": "mtop.taobao.iliad.comment.query.latest",
    "v": "1.0",
    "timeout": "10000",
    "preventFallback": "true",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp92",
    "data": data
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
show_barr(response.text)
