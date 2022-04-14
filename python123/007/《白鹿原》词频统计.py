'''附件是《白鹿原》原著内容，请读入内容，分词后输出长度大于 2 且最多的单词。
如果存在多个单词出现频率一致，请输出按照 Unicode 排序后最大的单词。'''

import jieba
d={}
file=open('D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\白鹿原.txt','r',encoding='utf-8')
f=file.read()     # ***
for word in jieba.lcut(f):   #*** 很多中文字段落且空格的 用 jieba.lcut() 函数
    if len(word)>1:
        d[word]=d.get(word,0)+1
d=list(d.items())
d.sort(key=lambda x:x[1],reverse=True)
print(d[0][0])


