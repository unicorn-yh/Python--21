dict1 = {'赵小明': '13299887777', '特明朗': '814666888', '普希京': '522888666', '吴小京': '13999887777'}
flag=0
key1=str(input())
value1=str(input())
if key1 in dict1:
    print("您输入的姓名在通讯录中已存在")
else:
    dict1[key1]=value1
    for key in dict1:
        print(key+':'+dict1[key])