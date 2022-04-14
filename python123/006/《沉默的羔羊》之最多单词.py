'''描述
附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于2且最多的单词。
如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。

输入格式
文件

输出格式
字符串
'''

import jieba
with open('沉默的羔羊.txt','r',encoding='utf-8')as f:
    t=f.read()
    wordlist={}    #字典类型: key为单词 value为单词出现的次数
    for word in jieba.lcut(t):
        if len(word)==1:continue   #单词长度小于2，不执行
        if word in wordlist.keys(): wordlist[word]+=1  #单词出现过，被记录在 wordlist里了
        else: wordlist[word]=1    #单词未出现过
maxNum=1
for key in wordlist.keys():
    if wordlist[key]>maxNum:
        maxNum=wordlist[key]     #更新 maxNum的最大值（单词出现次数）
        s=key                   #更新出现次数最高的单词              
print(s)