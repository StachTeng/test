import urllib.request

i=100
y=str(i)
url = 'https://placekitten.com/200/'+y
header = {"User-Agent":"Mozilla/5.0"}
req=urllib.request.Request(url,None,header)

response = urllib.request.urlopen(req)
hndx = response.read()
hndxx = hndx.decode("utf-8")
print(hndxx)

