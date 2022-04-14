'''将学生信息封装成一个类Student,包括姓名、性别、年龄、家庭住址。并在display()方法中显示这个信息。
输入：'张三','男',30,'寸金路29号'
输出：张三，男，30岁，寸金路29号。'''

class Student:
    '学生信息'
    def __init__(self,name,sex,age,address):
        self.name = name
        self.sex = sex
        self.age = age
        self.address = address
        
    def display(self):
        print(self.name+'，'+self.sex+'，'+str(self.age)+'岁，'+self.address+'。')
 
 
tmp = eval(input())
s1 = Student(*tmp)
s1.display()