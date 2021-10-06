# -*- coding = utf-8 -*- 
# @Time :2021/10/3 20:25
# @Author: stach  邓智强
# @File : zxcv.py
# @Software: PyCharm

import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter
import random
import re

class GetAgent:

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
            # print(str(proxy_temp)+"可以登陆")
            Proxy_list.append(proxy_temp)
            # Proxy_list.append([Type,ip,port])
        except:
            # print(str(proxy_temp)+"无法登陆")
            return

# class Tieba:
#     def __init__(self):  # 构造函数定义这个类的属性（变量）、函数
#         self.scratch()
#
#     def scratch(self):
#         comment = 'bais.txt'
#         T = '<span content=".*?" class=".*?">.*?</span>'
#         for i in range(1):
#             print("获取第" + str(i + 1) + "页")
#             url = "https://movie.douban.com/subject/1292052/comments?start=" + str(
#                 i * 20) + "&limit=20&status=P&sort=new_score"  # 确定要爬取的入口链接
#             # 模拟成浏览器并爬取对应的网页 谷歌浏览器
#             headers = {'User-Agent',
#                        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
#             opener = urllib.request.build_opener()
#             opener.addheaders = [headers]
#             data = opener.open(url).read().decode('utf8')
#             time_pattern = re.compile('<span content=".*?" class=".*?">(.*?)</span>', re.S)
#             time = re.findall(time_pattern, data)
#             id_pattern = re.compile('<h2><a href="https://movie.douban.com/review/(.*?)/', re.S)
#             id = re.findall(id_pattern, data)
#             for j in range(len(id)):
#                 html = 'https://movie.douban.com/j/review/' + str(id[j]) + '/full'
#                 data = opener.open(html).read().decode('utf8')
#                 html = data
#                 content_pattern = re.compile('data-original(.*?)main-author', re.S)
#                 content = re.findall(content_pattern, html)
#                 text_pattern = re.compile('[\u4e00-\u9fa5|，、“”‘’：！~@#￥【】*（）——+。；？]+', re.S)
#                 text = re.findall(text_pattern, content[0])
#                 text = ''.join(text)
#                 name_pattern = re.compile('data-author=.*?"(.*?)"', re.S)
#                 name = re.findall(name_pattern, html)
#                 with open(comment, 'a', encoding='utf-8-sig') as f:
#                     f.write(name[0].strip('\\') + '\n')
#                     f.write(time[j] + '\n')
#                     f.write(str(text) + '\n')
#                     f.write('\n')
#                     f.close()

if __name__ == "__main__":
    #批量获取访问ip
    header = {}  # header 可不可以在主函数里面用全局变量去定义？
    header[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

    Proxy_list = []  # 保存可用的IP 地址
    Tiezi_list = []  # 保存所有的帖子信息

    for i in range(0, 1):
        url = "http://www.ip3366.net/?stype=1&page=" + str(i)
        shuchu1 = GetAgent()
        print(shuchu1.IPlist)
        for ip, port, Type in shuchu1.IPlist:
            shuchu2 = TestProxy()

    workbook = xlsxwriter.Workbook('可用IP地址.xlsx')
    worksheet = workbook.add_worksheet()

    First_row = ['Type', 'ip', 'port']
    row = 0
    col = 0
    for each in First_row:
        worksheet.write(row, col, each)
        col = col + 1
    row = row + 1

    for each1 in range(0, len(Proxy_list)):
        for each2 in Proxy_list[each1]:
            worksheet.write(row, col, each2)
            col = col + 1
        row = row + 1
        col = 0

    workbook.close()
    print("IP地址存入成功")
