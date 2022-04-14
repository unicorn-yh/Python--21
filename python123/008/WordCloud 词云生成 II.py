'''wordcloud 是生成词云的 Python 第三方库，也是Python优秀的计算生态之一。
下面是一段生成词云的代码，但这段代码并不能如期产生理想的词云效果。请在不改变代码行数的情况下，修改代码，达到生成理想词云的目的。
'''
import wordcloud, jieba, random
# random.seed 和 random_state=random 用于保证输出结果不随机，便于评阅比对
random.seed(1)
c = wordcloud.WordCloud(font_path="msyh.ttc", random_state=random,background_color="black")
s = "新时代中国特色社会主义思想是全党全国人民为实现中华民族伟大复兴而奋斗的行动指南"
c.generate(" ".join(jieba.lcut(s)))
c.to_file("D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\outfile.png")