'''输入一个正整数 n，随机产生 10 个不超过 3 位的非负整数，将这些数字首尾相连以字符串形式输出。'''
import random
n=int(input())
random.seed(n)
for i in range(10):
    print("{}".format(random.randint(0,999)),end="")

    