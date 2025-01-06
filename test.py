import time

import requests

from dec.calljs import gen_sign

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
cookie = "t=a31b621e3b8a313e440780fc972ea602; thw=cn; ariaDefaultTheme=default; ariaFixed=true; ariaScale=1; ariaMousemode=true; ariaMouseten=true; ariaReadtype=1; ariaoldFixedStatus=false; ariaStatus=false; cookie2=17ba15f5c6a1529e2044f3db9bc601df; _tb_token_=5f891d5e79e7d; _samesite_flag_=true; havana_lgc2_0=eyJoaWQiOjI2NDE4MzI2MjIsInNnIjoiNGZmNjllN2I0MzNiNWE2ZjU5ZTBlNzhmY2EwOWQzZjUiLCJzaXRlIjowLCJ0b2tlbiI6IjFQMkt5MkpDR25URHdyNUVqMzJrcnd3In0; _hvn_lgc_=0; cookie3_bak=17ba15f5c6a1529e2044f3db9bc601df; cookie3_bak_exp=1735869166887; wk_cookie2=1291bcb23e28932df38e57ebcf8f26a7; wk_unb=UU6lTM6avvo1MA%3D%3D; env_bak=FM%2BgytvMDC8tgy1nZkOSpNwMABA0ZbdUN7eBC%2FQaTuZG; sdkSilent=1735900891836; havana_sdkSilent=1735900891836; xlly_s=1; 3PcFlag=1735874506032; sgcookie=E100RW7peBGsdrjBVNaKhrIE875dSxYPFRuF3%2BCXydi96sl8w3As55eqo46ebtJrXFQwCWPfIwJuwgA4Q59WPtNYOCGqI88VNou6qkxekYM6aX0%3D; havana_lgc_exp=1766978506077; unb=2641832622; uc1=pas=0&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie14=UoYdWNtd9xdZOQ%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D; sn=; uc3=vt3=F8dD37DlyRBv8uPYBtI%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&id2=UU6lTM6avvo1MA%3D%3D&nk2=u%2F4Bv2Rk; csg=1117cc25; lgc=%5Cu4E36%5Cu6653%5Cu82E5; cancelledSubSites=empty; cookie17=UU6lTM6avvo1MA%3D%3D; dnk=%5Cu4E36%5Cu6653%5Cu82E5; skt=1a91a79f7801fd25; existShop=MTczNTg3NDUwNg%3D%3D; uc4=id4=0%40U2xo%2FHIwwsjFEHxHqwj1EphOzsCG&nk4=0%40uQwldy5k10LTfzOSMK648zQ%3D; tracknick=%5Cu4E36%5Cu6653%5Cu82E5; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=%E8%8B%A52f; _nk_=%5Cu4E36%5Cu6653%5Cu82E5; cookie1=W8zKftpBnASmkq%2BMoN1p6u7ViANOJYzjhtCB0W3F8Rk%3D; fastSlient=1735874506080; cna=X9jCH6oEWxcCARsQm3LG01c/; mtop_partitioned_detect=1; _m_h5_tk=e3b82df1edd4128d8f4c6a1cddd12f3f_1735895208468; _m_h5_tk_enc=ecf7f64fb2ba159a2d62db0cb692ace4; tfstk=ghYIBzGvcJ2CmyyMtvhNh3LvrnQ73f8SuXPWiIBz8uQpC_pWTbjRUDv5VLJG2e7eTdGWLI-eFQchwTpJFT-EbqRHtab-3agquB0lB8pkFMCJ6NdGZzU-bMCGTkkr3xuq7DFOPvM2LyoUsc1fMaCd29Bt1_18eaIR9Ch1w_yL2ypJ6f6GiyUdpkF96s5RyTpRyfOOI_Gu0S1SA9AIOJ-0ydu4Ws6_yzL16YX6OVal6F5CjtdpRzU-q6sCHBBincHDfGdlVUVuPgOpmLfvpJHVxQK6C6_S7kQv13pfse34d1xe6IW9G7zytw15DaI_wzd1Jhjv-Z3YC1x9T3LHd7aRte8VVtjswzjPWESvDpNoiCQdwLjDzx4hpQdDon7j7kQv13pXVgo0ut1Q1uN1mz113fG_qubDUyAvSLKgBMCGOGls1JKlv1f13fG_qujds66Z1fwpq; isg=BMzMYx9Xx2ij0dPYPCG_eQZXnSr-BXCvbfRyISaMeHcasW-7RxMBPppHUbmJ-agH"
headers = {
    "user-agent": ua,
    "cookie": cookie
}
cookies = {
    "_m_h5_tk": "f726a146bdb9d4143788dcca79f31df4_1735879904051",
    "_m_h5_tk_enc": "a6961124192557b4d6f03fda9c7ae7f0",
}
url = "https://h5api.m.taobao.com/h5/mtop.taobao.iliad.comment.query.latest/1.0/"

token = "ecf7f64fb2ba159a2d62db0cb692ace4"
ts = int(time.time() * 1000)
appKey = 34675810
data = {"topic": "0b21fb37-503c-4476-8506-06f5b837f0db", "limit": 20, "tab": 2, "order": "asc", "paginationContext": "{\"commentId\":502170716999,\"refreshTime\":1735885128540,\"timestamp\":1735867641550}"}

params = {
    "appKey": appKey,
    "t": ts,
    "sign": gen_sign(token, ts, appKey, data),
    "data": data
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
