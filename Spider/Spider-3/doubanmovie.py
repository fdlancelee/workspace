import requests
import json
'''
如果返回的是json内容  可以用requests模块自带的  response.json() 直接转成Python 字典

或者引入json模块  用json.loads(response.content)

将返回内容 保存到文件里  

1
2
3
with open('xxxx.html','wb') as f:
 
　　f.write(response.content)
返回的内容转码  response.decode('utf-8')
'''


#定义请求url地址
url = "https://movie.douban.com/j/search_subjects"

#定义请求头
headers = {
    #"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

#范围0-100，步长20
for page_start in range(0,100,20):
    params = {
        "type": "movie",
        "tag": "热门",
        #"sort": "recommend",
        "page_limit": "20",
        "page_start": page_start
    }

    response =requests.get(
        url = url,
        headers = headers,
        params = params
        )
    
'''    
    # 方式一:直接转换json方法
    results = response.json()
    #print("results is ",results)
    #results.sorted(results,key=rate,reverse=True)
    #解析结果
'''  


    #response.text 返回响应内容，响应内容为 str 类型
    #respones.content 返回响应内容,响应内容为 bytes 类型
content = response.text
    # 转换成字符串
#string = content.decode('utf-8')
#content.sorted(content,key=rate,reverse=True)
    # 把字符串转成python数据类型
results = json.loads(content)  
    # 解析结果
for movie in results["subjects"]:
    print(movie["title"], movie["rate"])

'''
list方法，只能添加一个元素
    #解析结果
starred = []
for movie in results["subjects"]:
    join = movie["title"] + movie["rate"]
    starred.append(join)
    #print(movie["title"],movie["rate"])
    
print(starred)
'''