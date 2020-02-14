import datetime
def main():
#datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]) 
    begindate = datetime.date(2019,9,2)
    enddate = datetime.date(2019,9,20)
    reldate = enddate - begindate
    reldate = reldate.days
    print("begindate:",begindate)
    print("enddate:",enddate)
    print("实际天数:",reldate)

#//取整，%取余数
#获取期数和剩余天数
#从开户日开始算，第一期不用计算在内
    week = reldate//7
    dates = reldate%7
    print("一共付息期数:",week)   
    print("付息后剩余天数:",dates)

#本金
    #amount = 10000
#每期利息
    ench = 1253.39
#7天通知利息
    rate7date = 1.1
#活期利息
    ratecur = 0.3
#应付利息
#指定数字范围
#第一期不用计算是正常付息，从第二期开始，最后不足一期算一期
#range(start,stop[,step]),如range（1,3）则是1,2，不包含最后一个
    interest = 0
    print("利息差",rate7date-ratecur)
    i = 1
    for i in range(1,week+1):
        print(i)
        enchinterest = ench*1*(((rate7date-ratecur)/100)/360)*(reldate-i*7)
        #print('enchinterest',(enchinterest,ench,reldate-i*7))
        #interest += ench*i*(((rate7date-ratecur)/100)/360)*(reldate-i*7)
        interest += ench*1*(((rate7date-ratecur)/100)/360)*(reldate-i*7)
        print("第%d期,应付利息转本金为%f，本期计算天数%d，本期利息%f,应补给客户的利息为%f" %(i+1,ench*i,reldate-i*7,enchinterest,interest))       
main()

'''
#! /usr/bin/python3
# 打印5以内的整数，跳过2
for i in range(5):
    if i==2:        #如果i等于2，重新开始一次新的循环
        continue
    print(i)
'''