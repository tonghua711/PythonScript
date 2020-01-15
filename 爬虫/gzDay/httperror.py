#encoding:utf-8
import urllib.request
# req = urllib.request.Request("http://www.qq.com/")
req = urllib.request.Request("http://www.google.com/")

try:
    urllib.request.urlopen(req,timeout=2)
    # urllib.request.urlopen(req)

except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read().decode("utf8"))
except urllib.error.URLError as e:
    print('URL 无法访问')
    exit(0)
print('This is URL is ok!')