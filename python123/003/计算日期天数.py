from datetime import date
import time
import re
s=input()
y1=s[0:4]
m1=s[5:7]
d1=s[8:10]
begintime=date(int(y1),int(m1),int(d1))
y2=s[21:25]
m2=s[26:28]
d2=s[29:31]
endtime=date(int(y2),int(m2),int(d2))
ans=str(endtime-begintime)
print(re.sub('\D.*','',ans))  