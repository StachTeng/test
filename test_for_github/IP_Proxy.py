import urllib.request

header = {}
header={"User-Agent":"Mozilla/5.0"}
IP="120.196.112.6:3128"
proxy_temp={"http": "143.255.142.53: 8080"}
proxy_support=urllib.request.ProxyHandler(proxy_temp)
opener=urllib.request.build_opener(proxy_support)

try:
    req=urllib.request.Request("https://www.baidu,com",None,header)
    response=opener.open(req)
    print(IP+"国内可登录")
except:
    print("国内无法登陆")

try:
    req=urllib.request.Request("https://www.google,com",None,header)
    response=opener.open(req)
    print("国外可登录")
except:
    print("国外无法登陆")