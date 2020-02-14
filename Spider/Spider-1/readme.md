Kenneth Reitz 是 Python 领域的大神级人物，并且在 Github 上非常活跃，他的 Github 地址是：https://github.com/kennethreitz 
试着用所学知识去发现 Kenneth 今天 Starred 了哪些库，并且自动在浏览器中打开这些库的地址。

•   问题拆解提示：
•   本问题可以拆解为以下若干子问题：
•   1.如何获取指定用户所star的项目？
•   2.如何判断新的项目出现？
•   3.如何打开网页？
•   4.如何保持程序每隔一段时间进行监测？
•   问题解决提示：
•   1.通过GitHub提供的api，获取指定用户所star的所有项目，并转换为json数据。然后，将其中的id字段都提取出来，存入list变量。该变量即为用户已经star的项目的列表。api的调用格式为：https://api.github.com/users/kennethreitz/starred，其中kennethreitz是用户名，是可变参数。
•   2.重复1中的步骤，然后对比list变量和刚刚抓取的数据，如果项目id不在list变量中，说明该项目是新出现的。
•   3.利用webbrowser模块，其中的open函数可以控制浏览器打开一个指定的页面。
•   4.while True语句是一个死循环，即为一个可以无限循环下去的语句，该语句可以控制程序一直运行。time模块中的sleep函数，可以让程序休眠一段时间，从而达到了每隔一段时间再运行的效果。
