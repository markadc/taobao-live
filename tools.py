import json
import re

import requests as req


def make_token():
    """获取_m_h5_tk、_m_h5_tk_enc、token"""
    url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/?jsv=2.7.2&appKey=34675810&t=1735890542853&sign=1cf804046b8edeb4daa87919f51c176f&api=mtop.taobao.iliad.comment.query.latest&v=1.0&timeout=10000&preventFallback=true&type=jsonp&dataType=jsonp&callback=mtopjsonp26&data=%7B%22topic%22%3A%2271768acd-f0ca-4676-813a-49503916298c%22%2C%22limit%22%3A20%2C%22tab%22%3A2%2C%22order%22%3A%22asc%22%2C%22paginationContext%22%3A%22%7B%5C%22commentId%5C%22%3A502159776011%2C%5C%22refreshTime%5C%22%3A1735890543722%2C%5C%22timestamp%5C%22%3A1735859839804%7D%22%7D"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    headers = {"User-Agent": ua}
    res = req.get(url, headers=headers)
    cookies = res.cookies.get_dict()
    _m_h5_tk = cookies["_m_h5_tk"]
    _m_h5_tk_enc = cookies["_m_h5_tk_enc"]
    token = _m_h5_tk.split("_")[0]
    return _m_h5_tk, _m_h5_tk_enc, token


def jsonp2json(jsonp: str):
    data: dict = json.loads(re.match(".*?({.*}).*", jsonp, re.S).group(1))
    return data


def show_barr(jsonp: str):
    jsonData = jsonp2json(jsonp)
    for item in jsonData["data"]["comments"]:
        try:
            content = item["content"]
            username = item.get("tbNick") or item["renders"]["snsNick"]
            commentId = item["commentId"]
            print("{}：{}（{}）".format(username, content, commentId))
        except:
            pass
