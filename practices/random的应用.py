import random
random.seed(10)  
for i in range(3):
    r=random.randrange(10,100,10)  #步数10，[10,100)
    print(r)

print(random.uniform(10,100))  #10-100之间的小数
s=[1,2,3,4,5,6,7,8,9]
print(random.choice(s))
random.shuffle(s)
print(s)

for i in range(10):
    print(random.randint(10,999),end=",")   #随机[10,999]之间的整数