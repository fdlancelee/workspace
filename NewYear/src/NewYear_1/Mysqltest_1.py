'''
Created on 2016年1月8日

@author: FUDIAN
'''
import pymysql


conn = pymysql.connect(user='root',passwd='password',host='127.0.0.1',db='pythontest')
cur = conn.cursor()
cur.execute("select * from cino")
rs = cur.fetchall()
for r in rs:
    print('zoneno:',r[0])
    print(r)
    print('zoneno:',r[0])
cur.close()
conn.close()


