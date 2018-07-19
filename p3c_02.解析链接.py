# 3.1.3、解析链接
# urlparse
'''
from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)
'''
# urlunparse
'''
from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
'''
# urlsplit
'''
from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)
'''

# urlunsplit
'''
from urllib.parse import urlunsplit

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
'''
# urljoin
'''
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'htts://cuiqingcai.com/FAQ.html'))
'''
# urlencode
'''
from urllib.parse import urlencode

params = {
    'name':'germey',
    'age':'22'
}
base_url = 'http://www.baidu.com'
url = base_url + urlencode(params)
print(url)
'''
# parse_qs
'''
from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))
'''

# queto
'''
from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?id=' + quote(keyword)
print(url)
'''
# unquote
from urllib.parse import unquote

url = 'https://www.baidu.com/s?id=%E5%A3%81%E7%BA%B8'
print(unquote(url))