# 01-请求发送

# 01.01-urlopen
# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('UTF-8')) 打印玩野html源码
# print(type(response)) 打印返回的数据类型
''' 打印HTTPResponse的属性和方法
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
'''

# 01.02-data参数
'''
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('https://httpbin.org/post',data=data)
print(response.read())
'''

# 01.03-timeout参数
'''import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
print(response.read())
'''

# 在抛出异常的情况下，使用try，except跳出异常
'''import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT!')
'''

# 02.01-request：较为完整的请求
'''from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host':'httpbin.org'
}

dict1 = {
    'name':'Germey'
}

data = bytes(parse.urlencode(dict1), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
'''
# 03.01、异常处理URLError实例
''''from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
'''
# 03.02、HTTPError
''''from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
'''
# 03.03、先捕获子类再捕获父类
'''
from urllib import request, error
try:
    response = request.urlopen('https://www.cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successful')
'''