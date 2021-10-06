# -*- coding = utf-8 -*- 
# @Time :2021/10/3 22:41
# @Author: stach  邓智强
# @File : Douban.py
# @Software: PyCharm

import urllib.request
import re

comment = '肖生客的救赎.txt'
T = '<span content=".*?" class=".*?">.*?</span>'
for i in range(200):
    print("获取第"+str(i+1)+"页")
    url = "https://movie.douban.com/subject/1292052/reviews?start="+str(i*20)  # 确定要爬取的入口链接
    # 模拟成浏览器并爬取对应的网页 谷歌浏览器
    headers = {'User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read().decode('utf8')
    time_pattern = re.compile('<span content=".*?" class=".*?">(.*?)</span>', re.S)
    time = re.findall(time_pattern, data)
    id_pattern= re.compile('<h2><a href="https://movie.douban.com/review/(.*?)/', re.S)
    id= re.findall(id_pattern, data)
    for j in range(len(id)):
        html = 'https://movie.douban.com/j/review/' + str(id[j]) + '/full'
        data = opener.open(html).read().decode('utf8')
        html = data
        content_pattern = re.compile('data-original(.*?)main-author', re.S)
        content = re.findall(content_pattern, html)
        text_pattern = re.compile('[\u4e00-\u9fa5|，、“”‘’：！~@#￥【】*（）——+。；？]+', re.S)
        text = re.findall(text_pattern, content[0])
        text = ''.join(text)
        name_pattern = re.compile('data-author=.*?"(.*?)"', re.S)
        name = re.findall(name_pattern, html)
        with open(comment, 'a', encoding='utf-8-sig') as f:
            f.write(name[0].strip('\\') + '\n')
            f.write(time[j]+'\n')
            f.write(str(text) + '\n')
            f.write('\n')
            f.close()
