import requests


class Upload:
    def __init__(self, memberUid, cookies):
        self.uid = memberUid
        self.cookies = cookies
        self.header = {
            "Host": "webap.nkust.edu.tw",
            "Connection": "keep-alive",
            "Content-Length": "27",
            "Cache-Control": "max-age=0",
            "Origin": "http://webap.nkust.edu.tw",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "http://webap.nkust.edu.tw/nkust/index_main.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }

    def main(self):

        payload = {
            "etxt_std_skind": "99#社員",
            "etxt_std_count": "1",
            "etxt_std_id00": "學　　號",
            "etxt_std_kind00": "身份類別",
            "etxt_std_id01": "學　　號",
            "etxt_std_kind01": "身份類別",
            "chkbox11": "on",
            "etxt_std_id11": self.uid,
            "etxt_std_kind11": "未參與社團",
            "rtxt_std_kind11": "99",
            "rtxt_std_kind13": "09",
            "rtxt_std_kind15": "84",
            "rtxt_std_kind17": "H29",
            "rtxt_std_kind19": "01",
            "uni_id": "0523",
            "content": "  #{}#99#1".format(self.uid)
        }
        rs = requests.post(
            "http://webap.nkust.edu.tw/nkust/bk_pro/bk004_ins.jsp", data=payload, headers=self.header, cookies=self.cookies)
        return dict(result="done")
