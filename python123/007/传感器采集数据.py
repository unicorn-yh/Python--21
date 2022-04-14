'''下面是一个传感器采集数据文件 sensor-data.txt 的一部分：
其中，每行是一个读数，空格分隔多个含义，分别包括日期、时间、温度、湿度、光照和电压。其中，光照处于第 5 列。 
请编写程序，统计并输出传感器采集数据中光照部分的最大值、最小值和平均值，所有值保留小数点后 2 位。'''

f=open('D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\sensor-data.txt')
data=[]
average=total=0.0
for line in f:
    data.append(line.strip('\n').split(' '))
nmax=nmin=float(data[0][4])
for i in range(len(data)):
    d=float(data[i][4])
    if d>nmax: nmax=d
    if d<nmin: nmin=d
    total+=d
average=total/len(data)
print("最大值、最小值、平均值分别是：{:.2f},{:.2f},{:.2f}".format(nmax,nmin,average))

