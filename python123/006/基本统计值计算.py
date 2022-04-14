'''描述
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。
获取以逗号分隔的多个数据输入（输入为一行），计算基本统计值（平均值、标准差、中位数）
除中位数外，其他输出保留小数点后两位。
请补充编程模板中代码完成
'''

#请在...补充一行或多行代码
#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    return list(eval(input())) #list 类型

def mean(numbers):  #计算平均值
    total=0.0
    for n in numbers:
        total+=n
    return total/len(numbers)
    
def dev(numbers,mean): #计算标准差
    sdev=0.0
    for num in numbers:
        sdev+=(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):    #计算中位数
    numbers.sort()      #顺序排序list里的数字
    size=len(numbers)
    if size%2==0:
        return (numbers[size//2-1]+numbers[size//2])/2
    else:
        return numbers[size//2]   # // floor division, 除了得整数
    
n=getNum() #主体函数
m=mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))