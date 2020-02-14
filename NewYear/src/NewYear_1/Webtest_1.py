'''
Created on 2016年1月11日

@author: FUDIAN
'''
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']
    body = '<h1>Hello,%s!,</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode(encoding='utf_8')]