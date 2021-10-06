# -*- coding = utf-8 -*- 
# @Time :2021/10/4 10:59
# @Author: stach  邓智强
# @File : test6.py
# @Software: PyCharm

import requests
import re
import pandas as pd

def url_list():
    url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100020318814&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1"
    url_list=[url.format(i) for i in range(1,11)]
    return url_list
def url_parse(list):
    index = 1
    id_list = []
    content_list=[]
    time_list=[]
    for url in list:
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': 'https://item.jd.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        cookies = {
            '__jdu': '1140149181',
            'shshshfpb': 'dxvAdGKVNzAegFZ04SPRPjw==',
            'shshshfpa': '551d8e1b-9679-a2a9-4853-c893fad3a0c2-1588218470',
            'areaId': '13',
            'ipLoc-djd': '13-1042-3528-0',
            'unpl': 'V2_ZzNtbRBTFkYhDBZQeB4PBmIDEFwSXhYWcQERBykfWVFkBEcJclRCFnUUR1NnGFkUZwsZX0RcQBxFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsZWQRnBhpdS1dzJXI4dmR4HVsHZgIiXHJWc1chVERTcx1bACoDElhDV0YddQFGZHopXw==',
            '__jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_c5dbe5a526b24130a8d258fbc74e26de|1622806649582',
            '__jda': '122270672.1140149181.1607922153.1622723717.1622806650.7',
            '__jdc': '122270672',
            '_gcl_au': '1.1.1090722577.1622806657',
            'shshshfp': '2642ee3c640efeb0e9447e6545757fca',
            '__jdb': '122270672.5.1140149181|7.1622806650',
            'shshshsID': '3742c97b007a5cf7adaa9cff4323c957_3_1622806689501',
            'JSESSIONID': '81C1CD5FA9D0F18E7FFADD802EC34264.s1',
            'jwotest_product': '99',
            '3AB9D23F7A4B3C9B': '6NAODRKK6T33JSTFT3NYNWJAJQ2BCPHUZTUM73ZFAJPIMAS44RCYDE4BC6G7LRUPAWKISABMYIUWYB2LIDAMRKRPVU',
        }
        response = requests.get(url=url, headers=headers, cookies=cookies).text
        res_content = '"content":"(.*?)"'
        res_id = '"guid":"(.*?)"'
        res_time='"creationTime":"(.*?)"'
        content = re.findall(res_content, response)
        id= re.findall(res_id, response)
        time = re.findall(res_time, response)
        for i,c,t  in zip(id,content,time):
            id_list.append(i)
            content_list.append(c)
            time_list.append(t)
    print(id_list,content_list,time_list)
    return id_list,content_list,time_list
def excel(i,c,t):
    x=pd.DataFrame()
    x["时间"]=t
    x["ID"]=i
    x["评论内容"]=c
    x.to_excel("./京东评论.xlsx")

if __name__ == '__main__':
    list=url_list()
    i,c,t=url_parse(list)
    excel(i,c,t)

