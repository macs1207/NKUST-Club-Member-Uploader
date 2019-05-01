from Module import Login
from Module import Upload
import csv


def main():
    uid = ""
    pwd = ""
    cookies = Login.Login(uid=uid, pwd=pwd).main()
    with open("member.csv", "r", encoding="utf-8") as f:
        rows = csv.DictReader(f)
        for row in rows:
            result = Upload.Upload(
                memberUid=row["學號"], cookies=cookies).main()
            print("{}: {}".format(row["學號"], result))


main()
