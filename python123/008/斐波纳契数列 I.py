'''求斐波纳契（Fibonacci）数列：1, 1, 2, 3, 5, 8... 的前n项，n的值从键盘输入。'''
f=int(input())
n1,n2=0,1
s=[]
s.append("1")
for i in range(f-1):
    n3=n1+n2
    s.append(str(n3))
    n1=n2
    n2=n3
print(','.join(s))

#递归函数做法  直接统计总和
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+f(n-2)
