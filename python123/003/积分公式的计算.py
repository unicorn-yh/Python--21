i=int(input())
sum=0
for x in range(1,i+1):
    s=(1+1/x)**x
    sum+=s
print("{:.8f}".format(sum))


