'''有三个圆柱 A、B、C，初始时 A 上有 N 个圆盘，N 由用户输入给出，最终移动到圆柱 C 上。
每次移动步骤的表达方式示例如下：[STEP 10] A->C。其中，STEP 是步骤序号，宽度为 4 个字符，右对齐。
请编写代码，获得输入 N 后，输出汉诺塔移动的步骤。'''

steps=0
def hanoi(src,mid,des,n):
    global steps
    if n==1:
        steps+=1
        print("[STEP{:>4}] {}->{}".format(steps,src,des))
    else:
        hanoi(src,des,mid,n-1)
        steps+=1
        print("[STEP{:>4}] {}->{}".format(steps,src,des))
        hanoi(mid,src,des,n-1)
N = eval(input())
hanoi("A", "B", "C", N)

######
def hanoi(n,a,b,c):
    global steps
    if n==1:
        steps+=1
        print("{}:{}->{}".format(steps,a,c))
    else:
        hanoi(n-1,a,c,b)
        steps+=1
        print("{}:{}->{}".format(steps,a,c))
        hanoi(n-1,b,a,c)


count=1
def move(n,a,c):
    global count
    print("第{}步：将编号为{}的盘子从{}--->{}".format(count,n,a,c))
    count+=1

def hanoi(n,a,b,c):
    if n==1: 
        move(n,a,c)
    else:
        hanoi(n-1,a,c,b)
        move(n,a,c)
        hanoi(n-1,b,a,c)
    
if __name__=='__main__':
    n=int(input("请输入圆盘数量："))
    hanoi(n,"A","B","C")