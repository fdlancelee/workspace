import requests
import time
# 函数获取Star 数大于 200，topic 是 blockchain
def get_project(last_week,topic):
    api = 'https://api.github.com/search/repositories?q='
    query_created = 'created:>' + last_week
    query_topic = 'topics:>' + topic
    full_url = api + query_created + '+' + query_topic
    print("full_url is :",full_url)
    r = requests.get(full_url)
    #这里如果不做任何处理输出的话会返回请求的状态码
    print("r is :",r)
    print("r url :",r['items'])
    #定义一个空数组获取地址
    Urladd = []

    #for i in range(r.json)
    #return r.json()['items']


#函数实现短信发送
#但是由于要翻墙，暂时不做
'''
def push_it(message):
    api =  'https://api.pushover.net/1/messages.json/'
    # 此处需要两个指定身份的字符串，需要在网站注册才能获得
    data = {
        'app_token':'abcdefg',  #需要替换成你的token
        'user':'abcdefg',     #需要替换成你的user id
        'message':message
    }
    requests.post(api, data)
'''
last_week = "2018-03-3T00:00:00Z"
topic = 'blockchain'
get_project(last_week,topic)
'''
# 将符合条件的项目URL存入list变量中，便于查重
result = []
while True:
    #获取项目列表，搜条件为最近一周、blockchain相关
    project_list = get_project(last_week,topic)
    for p in project_list:
        stars = p['stargazers_count']
        # 如果项目符合条件，则调用push_it函数，发送到手机上
        if stars > 200 and not p['html_url'] in result:
            message = 'The project '+ p['name'] + ' is qualified.' + ' URL: ' + p['html_url']
            push_it(message)
            result.append(p['html_url'])
'''
