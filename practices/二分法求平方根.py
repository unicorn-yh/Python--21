'''设计一个用二分法计算一个大于或等于 1 的实数 n 的平方根的函数sqrt_binary(n)，
计算精度控制在计算结果的平方与输入的误差不大于1e-6。
第一行输出用自己设计的函数计算得到的平方根
第二行输出用math库开平方函数计算得到的平方根'''

def sqrt_binary(n):
    a,answer,b = 0,n/2,n
    while abs(answer**2 - n) > 1e-6:
        if answer**2>n:
            b = answer
        else:
            a = answer
        answer = (a + b)/2
    return answer
 
import math
n = eval(input())
print(sqrt_binary(n),math.sqrt(n),sep = '\n')