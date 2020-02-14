#20191126 学习网络爬虫
#导入request包
import requests
import cookies
import cookiejar
#定义请求地址
url = 'https://www.baidu.com/'
# 发送 GET 请求获取响应
response = requests.get(url)
# 获取响应的 html 内容
html = response.text
#html1 = response.content
'''
response 常用属性
response.text 返回响应内容，响应内容为 str 类型
respones.content 返回响应内容,响应内容为 bytes 类型
response.status_code 返回响应状态码
response.request.headers 返回请求头
response.headers 返回响应头
response.cookies 返回响应的 RequestsCookieJar 对象
'''
#print(html1)

# 获取字节数据
content = response.content
# 转换成字符串类型
html1 = content.decode('utf-8')
print('content.decode',html1)

#response.cookies 操作
# 返回 RequestsCookieJar 对象
cookies = response.cookies
print('cookies',cookies)

'''
# RequestsCookieJar 转 dict
requests.utils.dict_from_cookiejar(cookies)
# dict 转 RequestsCookieJar
requests.utils.cookiejar_from_dict()
# 对cookie进行操作,把一个字典添加到cookiejar中
requests.utils.add_dict_to_cookiejar()
'''

#返回请求头
headers = response.headers
print('headers is :',headers)

#发送请求时添加 headers 参数作为自定义请求头
'''
# 导入模块
import requests
# 定义请求地址
url = 'http://www.baidu.com'
# 定义自定义请求头
headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
# 发送自定义请求头
response = requests.get(url,headers=headers)
# 获取响应的 html 内容
html = response.text

'''

#发送请求时 params 参数作为 GET 请求参数
# 定义 GET 请求参数
'''
params = {
  "kw":"hello"
}
# 使用 GET 请求参数发送请求
response = requests.get(url,params=params)
# 获取响应的 html 内容
html = response.text
'''

#保存图片时后缀名和请求的后缀名一致
#保存必须使用 response.content 进行保存文件
# 下载图片地址
url1 = "http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png"
# 发送请求获取响应
response = requests.get(url1)
# 保存图片
# with open 文件读写完成后，自动调用close方法，保存在文件py文件所在目录
with open('image-pyhton.png','wb') as f:
  f.write(response.content)

#发送请求时 timeout 参数设置为超时秒数
'''
# 导入模块
import requests

url = "https://www.baidu.com"
# 设置忽略证书
response = requests.get(url,timeout=5)
'''

