import urllib
import requests
from requests.exceptions import RequestException
import re
#from bs4 import BeautifulSoup
import bs4
import json
import time
import chardet
#from lxml import etree
import lxml
from multiprocessing import Pool

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            print ("response.status_code is",response.status_code)
            #这里使用content可以直接返回结果，如果使用text如要对结果进行转换
            return response.text
        else:
            return None
    except RequestException:
        return None

def parse_one_page(html):
    #re模块中包含一个重要函数是compile(pattern [, flags]) ，该函数根据包含的正则表达式的字符串创建模式对象。
    #python会将字符串转换为正则表达式对象。而使用compile完成一次转换之后，在每次使用模式的时候就不用重复转换。
    pattern = re.compile(
        # re.S表示匹配任意字符，如果不加.无法匹配换行符
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    #print("items:",items)
    for item in items:
        ## 用yield的好处是可以迭代，利于多页输出
        print("**********item*******",item)
        yield {
            'index': item[0],
            'thumb': get_thumb(item[1]),
            'name': item[2],
            'star': item[3].strip()[3:],
            # 'time': item[4].strip()[5:],
            # 用函数分别提取time里的日期和地区
            'time': get_release_time(item[4].strip()[5:]),
            'area': get_release_area(item[4].strip()[5:]),
            'score': item[5].strip() + item[6].strip()
        }

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

# 数据存储到csv
def write_to_file(items):
    with open('猫眼top100.csv', 'a', encoding='utf_8_sig') as f:
        # 'a'为追加模式（添加）
        # utf_8_sig格式导出csv不乱码
        f.write(json.dumps(items, ensure_ascii=False) + '\n')
        print('第%s部电影爬取完毕' % items['index'])
        # items是字典形式，需用json.dumps转为字符串
        # json.dumps存数据时会使用unicode的16进制格式，所以中文在保存文件中是\u开头的,添加ensure_ascii =
        # False，即可保留中文


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    #print("html is :",html)

#提取方法 正则表达式
    for item in parse_one_page(html):
        print("item is :",item)
        write_to_file(item)
    #print("html is :",html)

if __name__ == "__main__":
    for i in range(1):
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
    
