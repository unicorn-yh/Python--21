'''
求解圆周率可以采用蒙特卡罗方法，在一个正方形中撒点，根据在 1/4 圆内点的数量占总撒点数的比例计算圆周率值。
'''
from random import *
DARTS=int(input())
hits=0.0
seed(123)
for i in range(1,DARTS+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:hits+=1
pi=4*(hits/DARTS)
print("{:.6f}".format(pi))