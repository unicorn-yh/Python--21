'''以整数 17 为随机数种子，获取用户输入整数 N 为长度，产生 3 个长度为 N 位的密码，密码的每位是一个数字。
每个密码单独一行输出。'''

import random

def genpwd(length):
    return random.randint(int(pow(10,length-1)),int(pow(10,length))-1)

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
