'''描述
已知变量s，编程统计并输出字符串 s 中汉字和标点符号的个数。'''

s = "学而时习之,不亦说乎?有朋自远方来,不亦乐乎?人不知而不愠,不亦君子乎?"
punctuation,ch=0,0
a=s.count(',',0,len(s))
for i in range(len(s)):
    if s[i]==',' or s[i]=='?':punctuation+=1
    else:ch+=1
print("字符数为{}，标点符号数为{}。".format(ch, punctuation))


#做法2
count1=s.count(",")
count2=s.count("?")
print("字符数为{}，标点符号数为{}。".format(len(s)-count1-count2,count1+count2 ))