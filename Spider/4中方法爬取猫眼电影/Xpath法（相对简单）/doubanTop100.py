from lxml import etree
import requests
import time

# https://mp.weixin.qq.com/s/LlT1vZFypn-kGKS57Qz0qA
#url = 'https://book.douban.com/top250'

# https://book.douban.com/top250?start=25
# start按照25的倍数改变
for start in range(4):
    url = 'https://book.douban.com/top250?start={}'.format(start*25)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
data = requests.get(url, headers=headers).text


s = etree.HTML(data)
'''
#获取名字 ok
#file = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/@title')
file = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')
for title in file:
    print("file name is :",file)
'''
'''
#获取评分 ok
pf = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')

for j in pf:
    print("pf is:",pf)
'''

'''
书面和评分复合输出 ok
file = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')
pf = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')

for i in range(10):
    print("{},{}".format(file[i],pf[i]))
'''

# 如果@title改为text()会存在错误，应该是每一本书全部进行抓取
# table[1]是定位序号，去掉就是取全部
#file = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]')
file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
for div in file:
    # 如果不加[0]返回的结果['撒哈拉的故事'],['9.0']，加了以后返回的结果 撒哈拉的故事,9.0
    title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
    score = div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]
    num = div.xpath(
        "./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")")
    print("{},{},{}".format(title, score, num))

    with open('豆瓣.csv', 'a', encoding='utf_8_sig') as f:
        # 'a'为追加模式（添加）
        # utf_8_sig格式导出csv不乱码
        f.write("{},{},{}".format(title, score, num) +'\n')
        

    time.sleep(10)

print('第{}部书爬取完成'.format(start))

'''
num出来后出现很多空格
追风筝的人,8.9,(
                    577793人评价
                )
        
使用strip() 方法，()里面表示要删除的内容，strip(“(”) 表示删除括号， strip() 表示删除空白符。

'''
