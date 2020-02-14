# coding:utf-8
import requests

"""
api形式 /code?q=language:python+size:<200+repo:目录名
q参数：
    language:指定语言
    size:指定文件大小，如size:<200表示文件小于200KB
    repo:指定目录（必要参数）
示例：
    https://api.github.com/search/code?q=language:python+size:<200+repo:tensorflow/tensorflow
"""
get_code_api = "https://api.github.com/search/code?q="
get_repo_api = "https://api.github.com/search/repositories?q=language:python"

# 编写函数，实现在github某一目录下寻找code文件的功能
def get_code(language, size, repo):
    url = get_code_api + "language:" + language + "+size:<" + size + "+repo:" + repo
    print('url is:',url)
    # 访问GitHub接口
    info = requests.get(url).json()
    #定义一个空数组
    Urladd = []
    if 'items' in info:
        for i in info['items']:
            print("1234:",i['html_url'])
            #Urladd.append(i['html_url'])
            #print(Urladd)
#get_code('python','200','tensorflow')

# 编写函数，查找更新时间在last_week之后的项目
def get_project(last_week):
    # 访问GitHub接口
    info = requests.get(get_repo_api).json()
    for i in info['items']:
        created_time = i['created_at']
        if created_time > last_week:
            language = "python"
            size = "200"
            # 从info数据中获取项目的目录
            # Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
            repo = i['html_url'].replace("https://github.com/", "")
            print("repo is :",repo)
            # 传入三个限制条件，调用查找code文件的函数
            get_code(language, size, repo)

get_project("2016-06-27T21:00:06Z")


            


