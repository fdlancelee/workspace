from lxml import etree
import requests
import time

url = 'http://www.endata.com.cn/BoxOffice/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
data = requests.get(url, headers=headers).text


s = etree.HTML(data)

#data输出结果是byte，要转换为str输出.使用decode方法
data = etree.tostring(s,encoding='utf-8').decode('GBK')
print(type(data),data)

#获取名字 ok
#file = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/@title')
file = s.xpath('//*[@id="TopRight"]/dl[1]/dd/h2')
print("____1____",file)
'''
for title in file:
    print("file name is :",file)
'''
