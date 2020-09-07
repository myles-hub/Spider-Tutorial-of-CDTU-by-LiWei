# urllib 模块学习

## 一、urllib2 模块介绍

urllib模块是分为 <u>**urllib**</u> 与 **<u>urllib2</u>** 2个版本的，现在的python3 已经将 **urllib** 与 **urllib2** 进行了合并，所以我们现在学习起来就方便了，我们只学习了了解 **<u>urllib2模块</u>** 就可以了。

### 1. 发起get请求

```python
# 导入模块
import urllib.request

# 准备 url
url = "http://httpbin.org/get"

# 发起get请求
response = urllib.request.urlopen(url)

# 读取源码，并解码
html_page = response.read().decode("utf-8")
print(html_page)
```



### 2. 发起post请求

```python
# 导入模块
import urllib.request

# 准备 url
url = "http://httpbin.org/post"

# 准备一个 data 请求参对象(data数据必须是字节流)
request = urllib.request.Request(url, data=b"hello=world")

# 发起 data 为二进制post请求
response = urllib.request.urlopen(request)

# 读取源码，并解码
html_page = response.read().decode("utf-8")
print(html_page)
```



###  3. 为请求添加 “headers”

```python
# 导入模块
import urllib.request

# 准备 url
url = "https://movie.douban.com/top250"

# 为解决 http 418报错，我们需要伪造一个 headers 头信息
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36"}
request = urllib.request.Request(url, headers=headers)

# 发起请求
response = urllib.request.urlopen(request)

# 读取源码，并解码
html_page1 = response.read().decode("utf-8")
print(html_page1)
```



## 二、urllib 四步下载

urllib.request(request) 是发起html文档对象下载的标准方法，基本步骤分为4步，具体总结如下。

### 1. 准备请求数据

- url = "http://httpbin.org/xxx"
- headers = {"k1":"v1"}
- data = b"hello=world"
- ...

### 2. 封装request请求对象

- request = urllib.requests(url, headers=headers, data)
- <u>**提示**：data数据类型必须是字节流</u>

### 3. 发起urlopne()请求

​    使用urlopen(request)发起 **<u>request请求</u>** ,获取 **<u>response响应对象</u>**

- response = urllib.request.urlopen(request)

### 4. 读取源码，并解码

​		从response中读取源码，并进行解码；

- html_page = response.read().decode('utf-8')



## 三、urlib 代码实例

```python
import urllib.request

try:
    # 1. 准备请求参数
    url = "https://movie.douban.com/top250"
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    # 2. 封装请求对象
    request = urllib.request.Request(url, headers=headers)

    # 3. 发起请求，获取响应对象
    response = urllib.request.urlopen(request)

    # 4. 读取源码，并解码
    html_page = response.read().decode()
execpt:
    pass
    
print(html_page)
```

