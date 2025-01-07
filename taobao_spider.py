import json
import queue
import re
import time
from functools import partial

import requests
from wauo.utils import cprint, cget, Loger

from dec import gen_sign

log = Loger(level="DEBUG")

prints = partial(cprint, color="red")

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


class TaobaoSpider():
    def __init__(self, live_id):
        self.live_id = live_id
        self.tk, self.tk_enc, self.token = self.make_token()
        log.success(
            """
            tk         {}
            tk_enc     {}"
            token      {}
            """.format(self.tk, self.tk_enc, self.token)
        )
        self.__topic = None
        self.q = queue.Queue()
        self.cache = []
        self.delay = 1
        self.max_delay = 3

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

    @property
    def topic(self):
        if self.__topic:
            return self.__topic
        self.__topic = self.crawl_topic(self.live_id)
        log.success(f"已获取到topic {self.__topic}")
        return self.__topic

    def bind_topic(self, value):
        self.__topic = value

    def parse_barrs(self, jsonp: str):
        """解析弹幕"""
        self.delay += 1
        self.delay = self.max_delay if self.delay >= self.max_delay else self.delay

        jsonData = jsonp2json(jsonp)
        comments = cget(jsonData, "data", "comments")
        if not comments:
            log.warning("无弹幕了")
            return

        for item in jsonData["data"]["comments"]:
            try:
                content = item["content"]
                username = item.get("tbNick") or item["renders"]["snsNick"]
                commentId = item["commentId"]
                cache = username, content, commentId
                if cache in self.cache:
                    continue
                self.delay = 1
                prints("{}：{}（{}）".format(*cache))
                self.cache.append(cache)
                item = dict(type="ChatMessage", name=username, content=content, uid="", head_img="")
                self.q.put(item)
            except:
                pass

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

    def crawl_barrs(self):
        """抓取弹幕"""
        log.debug("正在抓取弹幕...")

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
        self.parse_barrs(response.text)

    def listen(self):
        """监听直播间，弹幕消息推送到队列"""
        while True:
            self.crawl_barrs()
            time.sleep(self.delay)

    def pull_msg(self):
        """从队列拉取弹幕消息"""
        try:
            self.q.get(timeout=5)
        except queue.Empty:
            pass
        except Exception as e:
            log.error(e)


def test():
    import threading
    s = TaobaoSpider("502923558674")
    s.bind_topic("99b740b8-460a-413a-a8bb-db0b2baedd66")
    t = threading.Thread(target=s.listen)
    t.daemon = True
    t.start()
    time.sleep(1)
    while True:
        item = s.pull_msg()
        if item:
            log.info("从队列取到 => {}".format(item))


if __name__ == '__main__':
    # 胡可
    # live_id = "501743316235"
    # s = TaobaoSpider(live_id)
    # s.bind_topic("2b95ce32-e038-4fac-85f2-9ec2fd8f49bc")
    # s.crawl_barrages()

    # 其它
    # s = TaobaoSpider("502783187749")
    # print(s.topic)
    # s.crawl_barrages()

    test()
