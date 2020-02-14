# api https://api.github.com/repos/channelcat/sanic
# web_page https://github.com/channelcat/sanic
import requests
import webbrowser
import time
# api指定了follow的这个人star的所有项目，该用户是kennethreitz
api = "https://api.github.com/users/fdlancelee/starred"
api = "https://www.sogou.com"
# 先访问一次api，获取star列表


info = requests.get(api)
print(info.text)