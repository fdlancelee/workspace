import requests
from lxml import etree
import time

#从中国票房获取实时票房数据
url = 'https://maoyan.com/board/7'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

data = requests.get(url,headers=headers).text
#print("data is :",data)
datalist = etree.HTML(data)
#data输出结果是byte，要转换为str输出.使用decode方法
#dataresult = etree.tostring(datalist,encoding='utf-8')
#print(type(dataresult),dataresult)
#print("dataresult is:",dataresult.decode('utf-8'))

#尝试获取名字 
name = datalist.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a/@title')
print("1---1",name)