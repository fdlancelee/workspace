'''
网络获取数据
把响应数据转换成python数据类型
使用 jsonpath 提取数据
'''
# 网络获取数据
import requests
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
response = requests.get(url,headers=headers)
html = response.text
print(html)
# 把响应数据转换成python数据类型
data = json.loads(html)

'''
jsonpath 基本语法
$ 根节点
. 下一个节点
.. 子孙节点
[] 筛选条件，可以编写下标
'''


# 使用 jsonpath 提取数据
cities = jsonpath.jsonpath(data,'$..name')
print(cities)