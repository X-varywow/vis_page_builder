import json
import pandas as pd
import re
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import os
import time

from tqdm import tqdm  #进度条模块
from gen import gen    #负责生成html
from change_json import change_json

findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"')
findTitle = re.compile(r'<span class="title">(.*)</span>')
findJudge = re.compile(r'<span class="inq">(.*)</span>')

class menu:
    @staticmethod
    def show():
        print("1. 更新 vis.json【是否看过该电影的数据文件】")
        print("2. 生成html")
        print("3. 退出\n")

class pc:
    def __init__(self):
        self.head = {"Referer":"https://movie.douban.com/top250?start=25&filter=", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        self.data = None
        
    def ask_url(self, url):
        request = urllib.request.Request(url, headers =self.head)
        html = ""
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode("utf-8")
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)      
        return html
    
    def get_data(self, base_url):
        res = []
        pbar = tqdm(total = 250)
        
        for i in range(10):
            n = str(i*25)
            url = base_url + n
            html = self.ask_url(url)
            soup = BeautifulSoup(html, "html.parser")
            
            for item in soup.find_all("div", class_="item"):
                item = str(item)
                link = re.findall(findLink, item)[0]
                imgsrc = re.findall(findImgSrc, item)[0]
                title = re.findall(findTitle, item)[0]
                judge = re.findall(findJudge, item)
                if not judge:
                    judge = "暂无简介"
                else:
                    judge = judge[0]
                res.append([link,imgsrc,title,judge])
                pbar.update(1)
                
            time.sleep(0.5)
        pbar.close()
        return pd.DataFrame(res, index=range(1,251),columns=["link", "imgsrc", "title", "judge"])
        
    
    def run(self):
        os.system("cls")   #清空命令行
        print("正在爬取最新数据，请等待：\n\n")
        base_url = "https://movie.douban.com/top250?start="
        self.data = self.get_data(base_url)
        return self.data

    
if __name__ == "__main__":
    douban = pc()
    df = douban.run()

    menu.show()
    choice = (int(input("请输入选择：")))
    while choice != 3:
        if choice == 1:
            change_json(df.loc[:,"title"])
            menu.show()
            choice = (int(input("请输入选择：")))
        elif choice == 2:
            gen(df, "vis.json")
            print("已将文件生成于：{}\out.html ".format(os.getcwd()))
            choice = (int(input("请输入选择：")))
        else:
            choice = (int(input("请重新输入：")))

    print("\n程序已退出...")

    