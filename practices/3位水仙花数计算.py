'''"3位水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC.
请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。注意：这是一个OJ题目，输出格式要严格一致。'''

n = 0
for i in range(100,1000):
    m = str(i)
    a,b,c = list(m)[0],list(m)[1],list(m)[2]
    a,b,c,m = eval(a),eval(b),eval(c),eval(m)
    if m == a**3+b**3+c**3:
        if n == 0:
            print(m,end = '')
            n +=1
        else:
            print(",{}".format(m),end = '')