import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://tbzb.taobao.com/live?spm=a21bo.29164009%2Fevo632648b780028.discovery.d12_live.159f5f7eVlVaRb&liveSource=pc_live.discovery&liveId=501689839129",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "t": "a31b621e3b8a313e440780fc972ea602",
    "thw": "cn",
    "cna": "X9jCH6oEWxcCARsQm3LG01c/",
    "ariaDefaultTheme": "default",
    "ariaFixed": "true",
    "ariaScale": "1",
    "ariaMousemode": "true",
    "ariaMouseten": "true",
    "ariaReadtype": "1",
    "ariaoldFixedStatus": "false",
    "ariaStatus": "false",
    "xlly_s": "1",
    "cookie2": "17ba15f5c6a1529e2044f3db9bc601df",
    "_tb_token_": "5f891d5e79e7d",
    "_samesite_flag_": "true",
    "lgc": "%5Cu4E36%5Cu6653%5Cu82E5",
    "cancelledSubSites": "empty",
    "dnk": "%5Cu4E36%5Cu6653%5Cu82E5",
    "tracknick": "%5Cu4E36%5Cu6653%5Cu82E5",
    "havana_lgc2_0": "eyJoaWQiOjI2NDE4MzI2MjIsInNnIjoiNGZmNjllN2I0MzNiNWE2ZjU5ZTBlNzhmY2EwOWQzZjUiLCJzaXRlIjowLCJ0b2tlbiI6IjFQMkt5MkpDR25URHdyNUVqMzJrcnd3In0",
    "_hvn_lgc_": "0",
    "cookie3_bak": "17ba15f5c6a1529e2044f3db9bc601df",
    "cookie3_bak_exp": "1735869166887",
    "wk_cookie2": "1291bcb23e28932df38e57ebcf8f26a7",
    "wk_unb": "UU6lTM6avvo1MA%3D%3D",
    "env_bak": "FM%2BgytvMDC8tgy1nZkOSpNwMABA0ZbdUN7eBC%2FQaTuZG",
    "sdkSilent": "1735696375098",
    "havana_sdkSilent": "1735696375098",
    "3PcFlag": "1735612054836",
    "sgcookie": "E100gr9q8CbmcJWzges82ycdU%2FSnvQOSywyJVVtFl1OcYosP6soO0gLwSGZMoiivoTmRM%2FHku3hSNPShLJDJeoGQXZOqn9UFsaJxOFaDWzY5q3Q%3D",
    "havana_lgc_exp": "1766716054874",
    "unb": "2641832622",
    "uc1": "cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie21=Vq8l%2BKCLjA%2Bl&pas=0&cookie14=UoYdWNVDSTKdEQ%3D%3D&existShop=false",
    "sn": "",
    "uc3": "vt3=F8dD37DjrX%2BYqzNdN3Y%3D&id2=UU6lTM6avvo1MA%3D%3D&nk2=u%2F4Bv2Rk&lg2=UIHiLt3xD8xYTw%3D%3D",
    "csg": "ad654de8",
    "cookie17": "UU6lTM6avvo1MA%3D%3D",
    "skt": "0ef7372ca4b7e734",
    "existShop": "MTczNTYxMjA1NA%3D%3D",
    "uc4": "id4=0%40U2xo%2FHIwwsjFEHxHqwj1HFAVQj6z&nk4=0%40uQwldy5k10LTfzOc%2B67LVpM%3D",
    "_cc_": "U%2BGCWk%2F7og%3D%3D",
    "_l_g_": "Ug%3D%3D",
    "sg": "%E8%8B%A52f",
    "_nk_": "%5Cu4E36%5Cu6653%5Cu82E5",
    "cookie1": "W8zKftpBnASmkq%2BMoN1p6u7ViANOJYzjhtCB0W3F8Rk%3D",
    "fastSlient": "1735612054878",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "e200931c55019d4b2a9257caf78ce355_1735624562117",
    "_m_h5_tk_enc": "88da63ba111130a180a4663f8777ec04",
    "tfstk": "gwfEQiGzGWFecm_VfsArg4l0RnddSQrba_tWrabkRHxHV8ekUh70JHw8pgWNqGpBxg6IEbRd19GWAkdPriOzcoNbGwQp6QqbcCgHkvRpzv0HK0giSUdy-_KrBK7pwQqs5b2bgwIcy6Z5-UYg7UTStbjkEdxMXUMHqgxHIcY2kQAkZgxMIeTExUYkqVYMXUAkqgAu7Cx9zb45-acwlp4lV-54G7mpTnbHbbcqk3v3xNkSijfk8p5l-hJ6C18eLn99hH11tG_lO6pTIARR5tSPEgejBB7lKBYfJWlwiwX1aF17PY-hv17GOdujGiRF4KfHQ4cy9B-B_Ff0PxK1_HslTd4jgLOGGKAhCREBFB8Vq6IEzbjc5Z1pB_rqj3BBkCYfJWlwiwYl4inJSyo5w9ooUpY97naa744sfGl9TblIeYpMMF-bReM-epY97naa7YHJIELwcyTC.",
    "isg": "BK6uilDxRerXY7FG4rt9P1Dd_wRwr3Kpmy7Q39h1lrFsu0oVWTn1uiT9dydXY2rB"
}
url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/"
params = {
    "jsv": "2.7.2",
    "appKey": "34675810",
    "t": "1735615360775",
    "sign": "1a7625b23b3eb61e60272711e023a8f0",
    "data": "{\"topic\":\"f67b36e8-ec3a-4347-8f89-91b7ce2ec3c5\",\"limit\":20,\"tab\":2,\"order\":\"asc\",\"paginationContext\":\"{\\\"commentId\\\":501947807204,\\\"refreshTime\\\":1735615360150,\\\"timestamp\\\":1735615113000}\"}"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)