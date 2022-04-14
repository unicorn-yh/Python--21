weekstr="星期一星期二星期三星期四星期五星期六星期日";
weekid=eval(input("请输入星期数字(1-7):"))
index=(weekid-1)*3
print(weekstr[index:index+3])

for i in range(12):
    print(chr(9800+i),end="")

print(" ")
str="ab,ab,cd,ef,g"
print(str.count("ab"))
str=str.split(",")
print(str)
str="".join(str)
print(str.replace(",",""))
print("python".center(20,"="))
print("{0:=^20}".format("python"))
print("{0:*>20}".format("python"))
print("{0:*<20}".format("python"))
print("{:10}".format("BIT"))
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))


print("= python=".strip(" =np"))
print(" pyth on    ".strip())
print(",".join("12345"))

print(str[::-1])   #逆序串

for c in "python123":
    if c=='3':
        print(c,end='')
    else:
        print(c,end=",")

