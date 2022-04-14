'''对于一个列表，在保持非零元素相对顺序的同时，将元素中所有的数字0移动到末尾。
例如，获得输入列表 [0, 1, 0, 3, 12]，输出 [1, 3, 12, 0, 0].'''

ls = eval(input())
count = ls.count(0)
for i in range(count):
    ls.remove(0)
    ls.append(0)
print(ls)