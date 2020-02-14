'''
Created on 2016年1月11日

@author: FUDIAN
'''

from wsgiref.simple_server import make_server

from Webtest_1 import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
