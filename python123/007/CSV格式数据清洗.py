'''附件是一个 CSV 文件，其中每个数据前后存在空格，请对其进行清洗，要求如下：
1. 去掉每个数据前后空格，即数据之间仅用逗号 (,) 分割；
2. 清洗后打印输出。'''

f=open('D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\data.csv')
for line in f:
    line=line.replace(" ","")
    print(line,end="")