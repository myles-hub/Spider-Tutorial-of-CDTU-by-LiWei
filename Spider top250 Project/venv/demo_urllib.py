import urllib.request


# 发起get请求
# url = "http://httpbin.org/get"
# response = urllib.request.urlopen(url)
# html_page = response.read().decode()
# print(html_page)

# 发起post请求（data)
# url = "http://httpbin.org/post"
# response = urllib.request.urlopen(url, data=b'hello=world')
# html_page = response.read().decode()
# print(html_page)

requset = urllib.request.Request(url, data=b"hello=world")

response = urllib.request.urlopen(request)
html_page = response.read().decode("utf-8")
print(html_page)

# 为请求添加 headers

# 直接top250发起请求，会418报错了：urllib.error.HTTPError: HTTP Error 418:
# 418 报错原因分析：说明是爬虫客户端被服务识别了，因此被服务端禁止访问了；
# 解决方案：编辑一个请求头 header,以欺骗服务器端；

url = "https://movie.douban.com/top250"
headers = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36"}

# 编辑一个请求对象
request = urllib.request.Request(url,headers=headers)
# 对请求对象发起请求
response = urllib.request.urlopen(request)
html_page = response.read().decode()
print(html_page)