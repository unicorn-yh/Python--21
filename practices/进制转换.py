'''模块化程序设计是指在进行程序设计时将一个大的程序按照功能划分为若干小程序模块，每个小程序模块完成一个确定的功能，并在这些模块之间建立必要的联系，通过模块的互相协作完成整个功能。
请使用模块化程序设计方法完成进制转换，即：给你一个十进制数a（-65535<a<= 65535），将它转换成b（2 <= b <= 10）进制数输出(注意是：b是2-10之间的任意进制)。'''

#下面的函数求参数a的符号位并以字符串类型返回，‘-’表示负数，空串表示正数
def getSign(a):
    if a < 0:
        return '-'
    else:
        return ''
 
#下面的函数求整数absA的b进制表示，返回字符串
def getString(absA,b):
    bs = []
    while absA != 0:
        bs.append(str(absA%b))
        absA = absA//b 
    bs.reverse()
    b = "".join(bs)
    return b 
 
a=eval(input())
b=eval(input())
mark=getSign(a)
bitString=getString(abs(a),b)
print(mark+bitString)