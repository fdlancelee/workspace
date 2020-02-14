import webbrowser as web
#new:0：同一浏览器窗口打开 1：打开浏览器新的窗口，2：打开浏览器窗口新的tab #autoraise=True:窗口自动增长
#web.open('http://www.baidu.com',new=0,autoraise=True)                                              
#web.open_new('http://www.baidu.com')
web.open_new_tab('http://www.baidu.com')
