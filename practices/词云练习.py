import jieba,wordcloud
from imageio import imread
txt="人工智能的主题是学习， 从简单的机器学习到深度学习， 我们始终在头疼的一个事情就是过拟合。 对于过拟合， 我们有很多说法， \
    过拟合对应的是机器死记硬背， 没有能够举一反三的情况。 关于什么是泛化能力， 我们管它叫机器在新数据面前的预测水平。\
    用一个简单的方法理解过拟合，如果你手中的数据有限，比如说星空里观测到的三个星星，　你可以想象出任何一个复杂的图形穿过那三个点，\
        也是你的想象力丰富多彩，你就可以做出越多这样的图形。事实上，我们知道这样的想象不具备任何预测能力，如果天空中出现第四颗星，\
            我们一定就不能确定它是否在该在的位置上。"
w=wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttc")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\pywcloud.png")

mask=imread("D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\heart.png")
f=open("D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\白鹿原.txt","r",encoding="utf-8")
t=f.read()
txt=" ".join(jieba.lcut(t))
w=wordcloud.WordCloud(font_path="msyh.ttc",background_color="white",max_words=15,mask=mask)
w.generate(txt)
w.to_file("D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\bailuyuancloud.png")

f=open("D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\data.txt","r")
t=f.read()
txt=" ".join(jieba.lcut(t))
w=wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttc",background_color="white")
w.generate(txt)
w.to_file("D:\\yh\\YH2021\\Python\\Python语言程序设计\\document\\datacloud.png")


