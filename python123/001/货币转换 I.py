'''人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：
人民币和美元间汇率固定为：1 美元 = 6.78 人民币。
程序可以接受人民币或美元输入，转换为美元或人民币输出。
人民币采用 RMB 表示，美元 USD 表示，符号和数值之间没有空格。'''

currency=input()
if currency[0:3] in ['RMB']:
    usd=(eval(currency[3:]))/6.78
    print("USD{:.2f}".format(usd))
elif currency[0:3] in ['USD']:
    rmb=(eval(currency[3:]))*6.78
    print("RMB{:.2f}".format(rmb))