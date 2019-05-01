import requests


class Login:
    def __init__(self, uid, pwd):
        self.uid = uid
        self.pwd = pwd
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
            "uid": self.uid,
            "pwd": self.pwd
        }
        rs = requests.post(
            "http://webap.nkust.edu.tw/nkust/perchk.jsp", data=payload, headers=self.header)
        self.cookies = {}
        for i in rs.cookies:
            self.cookies[i.name] = i.value
        return self.cookies


if __name__ == "__main__":
    pass
