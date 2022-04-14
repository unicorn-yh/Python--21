import time
print(time.time())   #获取当前时间，计算机内部时间值
print(time.ctime())  #获取当前时间，字符串
print(time.gmtime()) #获取当前时间，计算机可处理的时间格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())) 