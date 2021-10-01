import urllib.request
from bs4 import BeautifulSoup

#创建Python函数

#定义打开网址的函数
def open_net(url):
    header = {"User-Agent":"Mozilla/5.0"}
    request=urllib.request.Request(url,None,header)
    response=urllib.request.urlopen(request)
    get_html=BeautifulSoup(response,'html.parser')
    return get_html

#定义爬取函数
def scractch(html):
    a_tag=html.findAll('a')
    a_list=[]
    for each in a_tag:
        if 'TOxiwmgRNSfffahp3g1tpg2/' in each['href']:
            if each['data-eid']=="qd_G55":
                char_name=each.text
                char_url="https://"+each['href']
                a_list.append([char_name,char_url])
    return a_list


#主函数调用
if __name__=='__main__':
    url='https://book.qidian.com/info/1030195954'
    html_after_open=open_net(url)
    novel_list=scractch(html_after_open)
    print(novel_list)