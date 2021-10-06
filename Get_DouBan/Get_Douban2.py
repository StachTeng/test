# -*- coding = utf-8 -*-
# @Time :2021/10/3 11:19
# @Author: stach  邓智强
# @File : Get_Douban2.py
# @Software: PyCharm

import urllib.request
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import random
import time


# import jieba
# import jieba.analyse
# from openpyxl import load_workbook
# import wordcloud

class GetAgent:#获取代理IP

    def __init__(self):  # 构造函数定义这个类的属性（变量）、函数

        self.IPlist = []
        self.open_net()
        self.scratch()

    def open_net(self):  # url 可不可以在主函数里面用全局变量去定义？

        req = urllib.request.Request(url, None, header)
        response = urllib.request.urlopen(req)
        html = response.read()
        return html

    def scratch(self):
        hhtml = BeautifulSoup(self.open_net(), "html.parser")
        hang = hhtml.findAll('tr')
        for each in range(0, len(hang)):
            try:
                lie = hang[each].findAll('td')
                self.IPlist.append([lie[0].text, lie[1].text, lie[3].text])
            except:
                continue


class TestProxy:

    def __init__(self):
        self.test()

    def test(self):

        proxy_host = ip + ":" + port
        proxy_temp = {Type: proxy_host}

        proxy_support = urllib.request.ProxyHandler(proxy_temp)
        opener = urllib.request.build_opener(proxy_support)

        try:
            req = urllib.request.Request("https://www.baidu.com", None, header)
            response = opener.open(req)
            print(str(proxy_temp)+"可以登陆")
            Proxy_list.append(proxy_temp)
            # Proxy_list.append([Type,ip,port])
        except:
            print(str(proxy_temp)+"无法登陆")
            return

class Douban:  # 爬取每一页的安居客房价信息（爬取海口的房价信息）
    def __init__(self):
        self.msg = []
        self.open_net()
        self.scratch()

    def open_net(self):  # url 可不可以在主函数里面用全局变量去定义？
        diaoyong = random.choice(Proxy_list)  # 随机调用代理 IP

        # 这里我们尝试一下使用requests库的get方法来获取response
        # req = requests.get(page_url,headers = header,timeout = 5)

        #然后再更改一下Windows里防火墙的访问

        #封装好req 请求对象
        req = urllib.request.Request(url=page_url, data=None, headers=header)

        #创建代理对象
        proxy_support=urllib.request.ProxyHandler(diaoyong)
        opener=urllib.request.build_opener(proxy_support)

        #通过代理opener来发送请求
        response=opener.open(req)

        html=response.read()
        return html

    def scratch(self):
        Html = BeautifulSoup(self.open_net(), "html.parser")
        # 爬取 要使用的应该是Beautifulsoup
        div = Html.find('div', {'id': 'content'})
        tbodys = div.find_all('div', {'class': 'main-bd'})
        # 返回tbody列表
        for each in range(1, len(tbodys)):
            try:
                # try:way = tbodys[each].find('em').contents[1].text
                # except:
                #     way=0
                try:
                    title = tbodys[each].find('div', {'class': 'short-content'}).text
                except:
                    title = 0
                try:
                    reply = tbodys[each].find('a', {'class': 'reply'}).text
                except:
                    reply = 0
                try:
                    zan = tbodys[each].find('span').text
                except:
                    zan = 0
                # try:reply = tbodys[each].find_all('a',{'c':'1'})[1].text
                # except:reply=0
                self.msg.append([title, reply, zan, ])
                print(title, reply, zan, )
            except:
                continue


if __name__ == "__main__":

    header = {}  # header 可不可以在主函数里面用全局变量去定义？
    header[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

    Proxy_list = []  # 保存可用的IP 地址
    #爬取代理IP并进行测试，测试函数将会把通过测试的代理IP存储到列表中仪表调用

    #爬取10页代理IP
    for i in range(1, 34):
        url = "http://www.66ip.cn/" + str(i) +'.html'
        shuchu1 = GetAgent()
        print(shuchu1.IPlist)
        for ip, port, Type in shuchu1.IPlist:
            shuchu2 = TestProxy()
    print(Proxy_list)


    #将爬取的IP地址写入文档 ，此处不进行存储，直接调用列表

    # workbook = xlsxwriter.Workbook('可用IP地址.xlsx')
    # worksheet = workbook.add_worksheet()
    #
    # First_row = ['Type', 'ip', 'port']
    # row = 0
    # col = 0
    # for each in First_row:
    #     worksheet.write(row, col, each)
    #     col = col + 1
    # row = row + 1
    # col = 0
    #
    # for each1 in range(0, len(Proxy_list)):
    #     for each2 in Proxy_list[each1]:
    #         worksheet.write(row, col, each2)
    #         col = col + 1
    #     row = row + 1
    #     col = 0
    #
    # workbook.close()
    # print("IP地址存入成功")

    # 利用代理爬取百度贴吧的帖子


    #创建IO流，打开文档，这里先不打开
    workbook2 = xlsxwriter.Workbook('豆瓣影评3.xlsx')  # 创建Excel文件
    worksheet2 = workbook2.add_worksheet()

    data_list = [ "评论内容", "回复数", "获赞数"]
    row, col = 0, 0
    for data in data_list:
        worksheet2.write(row, col, data)
        col += 1

    row, col = 1, 0

    header_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0']
    header_list.append(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31')
    header_list.append(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36')

    # 调用帖子信息爬取的类函数

    url1 = 'https://movie.douban.com/subject/1292052/reviews?start='
    #url2 = '.html'
    for i in range(1, 52):
        Message = []
        page_url = url1 + str(i*20) # + url2
        header['User-Agent'] = random.choice(header_list)
        Spider = Douban()
        Message = Spider.msg
        time.sleep(0.01)
        # print(Spider.msg)
        # 将爬取的信息存入 '豆瓣影评.xlsx'
        for j in range(0, len(Message)):
            for each in Message[j]:
                worksheet2.write(row, col, each)
                col = col + 1
            row = row + 1
            col = 0
            print("成功爬取部分豆瓣影评!"+str(j))
    workbook2.close()
    print('------------爬虫结束-------------')