# -*- coding = utf-8 -*- 
# @Time :2021/9/23 8:10
# @Author: stach  邓智强
# @File : 爬取IP地址存入Excel.by
# @Software: PyCharm

import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter

import random


# import time


# import jieba
# import jieba.analyse
# from openpyxl import load_workbook
# import wordcloud

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


class Tieba:  # 爬取每一页的贴吧帖子信息

    def __init__(self):  # 构造函数定义这个类的属性（变量）、函数
        self.scratch()

    def scratch(self):
        tieziliebiao = soup.findAll('ul', {'id': 'thread_list'})
        print(tieziliebiao)

        for each in tieziliebiao.findAll('li'):

            try:
                name = each.find('class' == 'j_th_tit ').text  # 帖子的主题
                print('haha1')
                content = each.find('class' == 'threadlist_abs threadlist_abs_onlyline ').text  # 帖子的内容
                print('haha2')
                author = each.find('class' == 'tb_icon_author').text  # 发帖人
                print('haha3')
                time = each.find('class' == 'pull-right is_show_create_time').text  # 发帖时间
                print('haha4')
                responser = each.find('class' == 'tb_icon_author_rely j_replyer ').text  # 最后回复人
                print('haha5')
                Tiezi = [name, content, author, time, responser]
                Tiezi_list.append(Tiezi)

            except:
                continue


if __name__ == "__main__":

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
    col = 0

    for each1 in range(0, len(Proxy_list)):
        for each2 in Proxy_list[each1]:
            worksheet.write(row, col, each2)
            col = col + 1
        row = row + 1
        col = 0

    workbook.close()
    print("IP地址存入成功")

    # 利用代理爬取百度贴吧的帖子

    url = "https://tieba.baidu.com/f?kw=%E6%B5%B7%E5%8D%97%E5%A4%A7%E5%AD%A6&ie=utf-8&pn="

    # print(Proxy_list)

    header_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0']
    header_list.append(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31')
    header_list.append(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36')

    for i in range(1, 3):
        page_url = url + str((i - 1) * 50)

        header['User-Agent'] = random.choice(header_list)  # 随机调用浏览器内核
        req = urllib.request.Request(page_url, None, header)

        diaoyong = random.choice(Proxy_list)  # 随机调用代理 IP

        print(diaoyong)

        proxy_support = urllib.request.ProxyHandler(diaoyong)
        opener = urllib.request.build_opener(proxy_support)
        response = opener.open(req)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        print(soup)

        shuchu3 = Tieba()  # 调用帖子信息爬取的类函数
        # time.sleep(0.1)

    workbook = xlsxwriter.Workbook(
        '海南大学贴吧.xlsx')  # 将爬取的信息存入 '海南大学贴吧.xlsx'                                              #创建Excel文件
    worksheet = workbook.add_worksheet()

    data_list = ["帖子的主题", "帖子的内容", "发帖人", "发帖时间", "最后回复人"]
    row, col = 0, 0
    for data in data_list:
        worksheet.write(row, col, data)
        col += 1
    row, col = 1, 0

    for each1 in range(0, len(Tiezi_list)):
        for each2 in Tiezi_list[each1]:
            worksheet.write(row, col, each2)
            col = col + 1
        row = row + 1
        col = 0

    workbook.close()

    print("帖子存入Excel完成")

