#用beautifulsoup + css选择器提取
import urllib
import requests
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup
import bs4
import json
import time
import chardet
from lxml import etree
import lxml
from multiprocessing import Pool
import csv

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            print("response.status_code is",response.status_code)
            #这里使用content可以直接返回结果，如果使用text如要对结果进行转换
            return response.text
        else:
            return None
    except RequestException:
        return None

##这个导入方法比较好用
def parse_one_page3(html):
    soup = BeautifulSoup(html, 'lxml')
    #print("soup is:",type(soup))
    items = range(100)
    for item in items:
        yield{
        # iclass节点完整地为'board-index board-index-1',写board-index即可
            'index':soup.select('dd i.board-index')[item].string,
        # 表示a节点下面的class =
        # board-img的img节点,注意浏览器eelement里面是src节点，而network里面是data-src节点，要用这个才能正确返回值
        # 通过子标签查找select('a > img.board-img')
            'thumb': get_thumb(soup.select('a > img.board-img')[item]["data-src"]),
            'name': soup.select('.name a')[item].string,
        #select('.star')通过类名查找
            'star': soup.select('.star')[item].string.strip()[3:],
            'time': get_release_time(soup.select('.releasetime')[item].string.strip()[5:]),
        # str.strip([chars])需要去掉的特殊字符。从字符串起始至末尾去掉chars。默认去掉字符串中的空格。
            'area': get_release_area(soup.select('.releasetime')[item].string.strip()[5:]),
            'score': soup.select('.integer')[item].string + soup.select('.fraction')[item].string
        #通过ID查找 print soup.select('#link1')
        }
        
    

def write_to_file3(item):
    with open('猫眼top100css.csv', 'a', encoding='utf_8_sig', newline='') as f:
        w = csv.writer(f)
        # w.writerow(dict.keys())
        w.writerow(item.values())
        # 添加newline=''防止产生空行

# 获取封面大图
# http://p0.meituan.net/movie/5420be40e3b755ffe04779b9b199e935256906.jpg@160w_220h_1e_1c
# 去掉@160w_220h_1e_1c就是大图
def get_thumb(url):
    pattern = re.compile(r'(.*?)@.*?')
    thumb = re.search(pattern, url)
    return thumb.group(1)

# 提取时间函数
def get_release_time(data):
    pattern = re.compile(r'(.*?)(\(|$)')
    items = re.search(pattern, data)
    if items is None:
        return '未知'
    return items.group(1)  # 返回匹配到的第一个括号(.*?)中结果即时间


# 提取国家函数
def get_release_area(data):
    pattern = re.compile(r'.*\((.*)\)')
    # $表示匹配一行字符串的结尾，这里就是(.*?)；\(|$,表示匹配字符串含有(,或者只有(.*?)
    items = re.search(pattern, data)
    if items is None:
        return '未知'
    return items.group(1)    




def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    #print("html is :",html)

#提取方法 正则表达式
    for item in parse_one_page3(html):
        print("item is :",item)
        write_to_file3(item)
    #print("html is :",html)

if __name__ == "__main__":
    for i in range(2):
        # time.sleep(0.5)
        # 猫眼增加了反爬虫，设置0.5s的延迟时间
        main(i*10)
        time.sleep(1)

'''
#使用多进程提升爬取效率
if __name__ == "__main__":
    pool = Pool()
    pool.map(main,[i*10 for i in range(1)])
'''
    
