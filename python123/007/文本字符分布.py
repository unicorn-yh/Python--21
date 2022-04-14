'''分析附件 data.txt 文件的字符分布，即每个字符对应的数量.
按照 字符：数量 显示，每行一个结果，如果没有出现该字节则不显示输出，字符采用 Unicode 编码升序排列。'''

#做法1
f=open('D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\data.txt')
d={}
for line in f:
    for c in line:
        d[ord(c)]=d.get(ord(c),0)+1
d=list(d.items())
d.sort(key=lambda x:x[0],reverse=False)
for i in range(len(d)):
    print("{}:{}".format(chr(d[i][0]),d[i][1]))

#做法2
f=open('D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\data.txt')
d={}
for line in f:
    for c in line:
        d[c]=d.get(c,0)+1
d=list(d.items())
d.sort(key=lambda x:x[0])
for i in range(len(d)):
    print("{}:{}".format(d[i][0],d[i][1]))