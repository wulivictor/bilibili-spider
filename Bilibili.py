import json
import sys
import requests
from you_get import common as you_get

def down(uid, page_size, page):
    url = "https://api.bilibili.com/x/space/arc/search?mid={0}&ps={1}&tid=0&pn={2}&keyword=&order=pubdate&jsonp=jsonp"
    url = url.format(uid, page_size, page)
    print(url)
    res = requests.get(url)
    data = res.text
    data = json.loads(data)
    list = data["data"]["list"]["vlist"]
    count = data["data"]["page"]["count"]
    print(list)
    video_url = "https://www.bilibili.com/video/{0}"
    for o in list:
        v_url = video_url.format(o["bvid"])
        print(v_url)
        sys.argv = ['you-get', '-o', "D:/video", v_url]
        you_get.main()
    return count, list

if __name__ == "__main__":

    uid = input("请输入up主的 uid：")
    page = 1
    page_size = 30
    count, list = down(uid, page_size, page)
    for i in range(count - 1):
        page = page + 1
        down(uid, page_size, page)