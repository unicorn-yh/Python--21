str=input();
s=[]
for i in range(len(str)):
    if str[i].islower() or str[i].isupper():  #是字母
        p=ord(str[i])
        if(p<123-3 or p<91-3):
            s.append(chr(p+3))
        else:
            s.append(chr(p+3-26))
    else:
        s.append(str[i])
print(''.join(s))