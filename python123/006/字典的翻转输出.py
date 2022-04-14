'''描述
读入一个字典类型的字符串，反转其中键值对输出。
即，读入字典key:value模式，输出value:key模式。

输入格式
用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。

输出格式
给定字典d，按照print(d)方式输出
'''

#第一种做法
d=eval(input())
try:
    reverse={}     #定义 reverse为dict类型
    for key in d:
        reverse[d[key]]=key   #d[key]=d该key的values
    print(reverse)
except:
    print("输入错误")

#第二种做法
d=eval(input())
try:
    value=list(d.values())
    key=list(d.keys())
    reverse={}     
    for i in range(len(value)):
        reverse[value[i]]=key[i]
    print(reverse)
except:
    print("输入错误")