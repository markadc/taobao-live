import json
import re
import time
from functools import partial

import requests
from loguru import logger
from wauo.utils import cprint

from dec import gen_sign

print = partial(cprint, color="red")

session = requests.Session()
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/131.0.0.0"
headers = {"User-Agent": ua}


def mills():
    """毫秒时间戳"""
    ts = time.time()
    return str(int(ts * 1000))


def jsonp2json(jsonp: str):
    data: dict = json.loads(re.match(".*?({.*}).*", jsonp, re.S).group(1))
    return data


def show_barr(jsonp: str):
    """测试用，展示弹幕"""
    jsonData = jsonp2json(jsonp)
    for item in jsonData["data"]["comments"]:
        try:
            content = item["content"]
            username = item.get("tbNick") or item["renders"]["snsNick"]
            commentId = item["commentId"]
            print("{}：{}（{}）".format(username, content, commentId))
        except:
            pass


class TaobaoSpider():
    def __init__(self, live_id):
        self.live_id = live_id
        self.tk, self.tk_enc, self.token = self.make_token()
        logger.success("已获取到tk、tk_enc、token")
        self.__topic = None

    def update_topic(self, value):
        self.__topic = value

    @property
    def topic(self):
        if self.__topic:
            return self.__topic
        self.__topic = self.crawl_topic(self.live_id)
        return self.__topic

    @staticmethod
    def make_token():
        """获取_m_h5_tk、_m_h5_tk_enc、token"""
        url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/?jsv=2.7.2&appKey=34675810&t=1735890542853&sign=1cf804046b8edeb4daa87919f51c176f&api=mtop.taobao.iliad.comment.query.latest&v=1.0&timeout=10000&preventFallback=true&type=jsonp&dataType=jsonp&callback=mtopjsonp26&data=%7B%22topic%22%3A%2271768acd-f0ca-4676-813a-49503916298c%22%2C%22limit%22%3A20%2C%22tab%22%3A2%2C%22order%22%3A%22asc%22%2C%22paginationContext%22%3A%22%7B%5C%22commentId%5C%22%3A502159776011%2C%5C%22refreshTime%5C%22%3A1735890543722%2C%5C%22timestamp%5C%22%3A1735859839804%7D%22%7D"
        res = session.get(url, headers=headers)
        cookies = res.cookies.get_dict()
        tk = cookies["_m_h5_tk"]
        tk_enc = cookies["_m_h5_tk_enc"]
        token = tk.split("_")[0]
        return tk, tk_enc, token

    def crawl_topic(self, live_id):
        url = "https://h5api.m.taobao.com/h5/mtop.tblive.live.detail.query/4.0/"
        ts = mills()
        appKey = "34675810"
        data = '{"liveId":"%s","productType":"live","liveSource":"source_pc_live","entryLiveSource":"source_pc_live","useLiveFandom":false}' % live_id
        sign = gen_sign(self.token, ts, appKey, data)
        params = {
            "jsv": "2.7.2",
            "appKey": appKey,
            "t": ts,
            "sign": sign,
            "api": "mtop.tblive.live.detail.query",
            "v": "4.0",
            "timeout": "10000",
            "preventFallback": "true",
            "type": "jsonp",
            "dataType": "jsonp",
            "callback": "mtopjsonp2",
            "data": data
        }
        headers["Referer"] = "https://tbzb.taobao.com/live"
        res = session.get(url, headers=headers, params=params)
        jsonData = jsonp2json(res.text)
        topic = jsonData["data"]["topic"]
        return topic

    def crawl_barrages(self):
        appKey = "34675810"
        ts = mills()
        data = '{"topic":"%s","limit":20,"tab":2,"order":"asc"}' % self.topic
        sign = gen_sign(self.token, ts, appKey, data)
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
        response = session.get(url, headers=headers, params=params)
        show_barr(response.text)


if __name__ == '__main__':
    # 胡可
    # live_id = "501743316235"
    # s = TaobaoSpider(live_id)
    # s.update_topic("2b95ce32-e038-4fac-85f2-9ec2fd8f49bc")
    # s.crawl_barrages()

    # 其它
    s = TaobaoSpider("502783187749")
    s.crawl_barrages()
