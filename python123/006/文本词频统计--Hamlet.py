'''' 统计哈姆雷特中词频为前十的单词：'''

def getText():
    txt=(open("hamlet.txt","r").read()).lower()
    for c in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt=txt.replace(c,"")
    return txt
count={}                               #count
for word in getText().split():
    count[word]=count.get(word,0)+1   #获取word出现的次数
items=list(count.items())             #用list列表形式定义字典 count
items.sort(key=lambda x:x[1],reverse=True)  #key的第二个元素，倒序倒排
for i in range(10):
    word,count=items[i]
    print(word) 
    #或者 print(items[i][0])  