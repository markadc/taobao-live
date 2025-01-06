from pathlib import Path


def gen_sign(token, ts, appKey, data) -> str:
    """淘宝的sign"""
    import subprocess
    from functools import partial
    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
    import execjs
    jsFile = (Path(__file__).parent / "tb_sign.js").absolute()
    with open(jsFile, encoding='utf-8') as f:
        jsCode = f.read()
    tb_sign = execjs.compile(jsCode).call('gen_sign', token, ts, appKey, data)
    return tb_sign


if __name__ == '__main__':
    token = "816dcced2e473e49e4812b4931d8bd6b"
    ts = "1735875895561"
    appKey = "12574478"
    data = '{"appId":"43356","params":"{\\"device\\":\\"HMA-AL00\\",\\"isBeta\\":\\"false\\",\\"grayHair\\":\\"false\\",\\"from\\":\\"nt_history\\",\\"brand\\":\\"HUAWEI\\",\\"info\\":\\"wifi\\",\\"index\\":\\"4\\",\\"rainbow\\":\\"\\",\\"schemaType\\":\\"auction\\",\\"elderHome\\":\\"false\\",\\"isEnterSrpSearch\\":\\"true\\",\\"newSearch\\":\\"false\\",\\"network\\":\\"wifi\\",\\"subtype\\":\\"\\",\\"hasPreposeFilter\\":\\"false\\",\\"prepositionVersion\\":\\"v2\\",\\"client_os\\":\\"Android\\",\\"gpsEnabled\\":\\"false\\",\\"searchDoorFrom\\":\\"srp\\",\\"debug_rerankNewOpenCard\\":\\"false\\",\\"homePageVersion\\":\\"v7\\",\\"searchElderHomeOpen\\":\\"false\\",\\"search_action\\":\\"initiative\\",\\"sugg\\":\\"_4_1\\",\\"sversion\\":\\"13.6\\",\\"style\\":\\"list\\",\\"ttid\\":\\"600000@taobao_pc_10.7.0\\",\\"needTabs\\":\\"true\\",\\"areaCode\\":\\"CN\\",\\"vm\\":\\"nw\\",\\"countryNum\\":\\"156\\",\\"m\\":\\"pc_sem\\",\\"page\\":1,\\"n\\":48,\\"q\\":\\"app11\\",\\"qSource\\":\\"url\\",\\"pageSource\\":\\"\\",\\"tab\\":\\"all\\",\\"pageSize\\":48,\\"totalPage\\":100,\\"totalResults\\":4800,\\"sourceS\\":\\"0\\",\\"sort\\":\\"_coefp\\",\\"bcoffset\\":\\"\\",\\"ntoffset\\":\\"\\",\\"filterTag\\":\\"\\",\\"service\\":\\"\\",\\"prop\\":\\"\\",\\"loc\\":\\"\\",\\"start_price\\":null,\\"end_price\\":null,\\"startPrice\\":null,\\"endPrice\\":null,\\"itemIds\\":null,\\"p4pIds\\":null,\\"categoryp\\":\\"\\",\\"myCNA\\":\\"X9jCH6oEWxcCARsQm3LG01c/\\"}"}'
    print(gen_sign(token, ts, appKey, data))
