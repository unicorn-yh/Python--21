'''字符串反码的定义为：字符串所包含字符的反码组成的字符串。
字符反码的定义为：
(1) 对于小写英文字符，它的反码也是一个小写英文字符，且该字符与'a'的距离等于其反码与'z'的距离；
(2) 对于大写英文字符，它的反码也是一个大写英文字符，且该字符与'A'的距离等于其反码与'Z'的距离；
两个字符距离指其对应unicode编码之差。
输入：2018-Python123-Well-Done
输出：2018-Kbgslm123-Dvoo-Wlmv'''

strIn = input()
for i in strIn:
    if i.islower()==True:
        print("{}".format(chr(ord('z')+ord('a')-ord(i))),end="")
    elif i.isupper()==True:
        print("{}".format(chr(ord('Z')+ord('A')-ord(i))),end="")
    else:
        print(i,end="")