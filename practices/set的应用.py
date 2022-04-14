

ls=list('3,2,1,5,6,4')
ls=sorted(ls,reverse=True)   #逆序排序
print(ls)
ls=set(ls)
print(ls)
ls.remove(",")
print(ls)
ls=sorted(ls)
print(ls)
ls=list(ls)
ls.sort(reverse=True)
print(ls)

for item in [123,"py",456]:
	print(item,end="")
