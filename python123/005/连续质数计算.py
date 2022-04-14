'''获得用户输入数字 N，计算并输出从 N 开始的 5 个质数，单行输出，质数间用逗号、分割。
注意：需要考虑用户输入的数字 N 可能是浮点数，应对输入取整数；最后一个输出后不用逗号。'''

def prime(m):
    for i in range(2,m):
        if m%i==0:
            return False
    return True
temp=eval(input())
n=temp
if n!=int(n):
    n=int(n)+1
else:
    n=int(n)
count=0
s=[]
while count<5:
    if prime(n):
        s.append(str(n))
        count+=1
        if count!=5:
            s.append(",")
    n+=1
print(''.join(s))

#做法2
n=temp
count=0
while count<5:
    if prime(n):
        print(n) if count==4 else print(n,end=",")
        count+=1
    n+=1
