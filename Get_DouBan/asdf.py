# -*- coding = utf-8 -*- 
# @Time :2021/10/3 20:05
# @Author: stach  邓智强
# @File : asdf.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

header = {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

for i in range(1,20):
    url = "https://movie.douban.com/subject/1292052/comments?start="+str(i*20)+"&limit=20&status=P&sort=new_score"
    res= requests.get(url, headers=header)

    res=BeautifulSoup(res.text,"lxml")
    comments = res.find("div",id="comments")
    p_list=comments.find_all("p")
    data_list=[]
    for i in p_list:
        data_list.append(i.find("span").string)

with open("肖生克的救赎.txt","w") as f:
    for i in data_list:
        f.write(i+"\n")