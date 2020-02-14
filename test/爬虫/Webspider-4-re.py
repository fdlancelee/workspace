import re
result = re.match("hello","hello.cn")
result.group()
print(result.group())

'''
常见语法
字符

语法  说明  表达式案例   完整匹配字符串
一般字符    匹配自身    abc abc
.   匹配任意除换行符\n外的字符。在DOTALL模式中也能匹配换行符    a.c abc
\   转义字符，使后一个字符表示字符本身。  a.c a.c
[...]   选取字符范围  a[bcd]e abe 或 ace 或 ade
预定义字符集（可以写在字符集[...]中）

语法  说明  表达式案例   完整匹配字符串
\d  数字:[0-9]    a\dc    a1c
\D  非数字:[^0-9]  a\Dc    abc
\s  空白字符:[<空格>\t\r\n\f\v]   a\sc    a c
\S  非空白字符:[^<空格>\t\r\n\f\v] a\Sc    abc
\w  单词字符:[A-Za-z0-9_]   a\wc    abc
\W  非单词字符:[^A-Za-z0-9_] a\Wc    a c
数量词（用在字符或(...)之后）

语法  说明  表达式案例   完整匹配字符串
*   匹配前一个字符0次或无限次。  abc*    abccc
+   匹配前一个字符1次或无限次。  abc+    abccc
?   匹配前一个字符0次或1次。   abc?    abc 或 ab
{m} 匹配前一个字符m次。  ab{2}c  abbc

1. 匹配开头和结尾的正则表达式
代码  功能
^   匹配字符串开头
$   匹配字符串结尾


四大检索方法
match 开头匹配，只匹配一次
search 全局匹配，只匹配一次
findall 匹配所有符号条件的数据，返回是 结果列表
finditer 迭代对象，迭代 Match 对象
'''