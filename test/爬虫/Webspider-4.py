#04 - 数据提取概念和数据的分类
#05 - JSON数据提取
'''
json.loads json字符串 转 Python数据类型
json.dumps Python数据类型 转 json字符串
json.load json文件 转 Python数据类型
json.dump Python数据类型 转 json文件
ensure_ascii=False 实现让中文写入的时候保持为中文
indent=空格数 通过空格的数量进行缩紧
'''
import json

rootdir = "D:/Python/filetext"

# json.loads json字符串 转 Python数据类型
json_string = '''
{
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
'''
#dict 用于创建一个数据字典
print("json_string数据类型：",type(json_string))
data = json.loads(json_string)
print("data数据类型：",type(data))
print("data：",data)
print("*" * 100)

# json.dumps Python数据类型 转 json字符串
data = {
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
print("data数据类型：",type(data))
json_string = json.dumps(data)
print("json_string数据类型：",type(json_string))
print(json_string)

print("*"*100)
# json.load json文件 转 Python数据类型
# notepad++打开文件   -> 格式 ->以utf-8无bom模式编码 ->保存
with open('D:/Python/workspace/test/爬虫/file/data.json','r',encoding='utf-8') as f:
    data = json.load(f)
    print("data数据类型：", type(data))
    print(data)

print("*"*100)

# json.dump Python数据类型 转 json文件
data1 = {
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
with open('D:/Python/workspace/test/爬虫/file/data_out.json','w',encoding='utf-8') as f:
    json.dump(data1,f,ensure_ascii=False,indent=2)