dt = {
    "姓名":["张唐","李丽"],
    "学号":["201805160021","201805160022"],
    "成绩":{
        "英语":[89,95],
        "政治":[98,80],
        "Python程序设计":[90,95]
    }
}
for a in range(2):
    ave=(dt['成绩']['英语'][a]+dt['成绩']['政治'][a]+dt['成绩']['Python程序设计'][a])/3
    print("{} 英语、政治、Python三门课程平均成绩为: {:.1f}".format(dt["姓名"][a],ave))


for item in dt.items():
    if item[1]==["张唐","李丽"]:
        print(item[0])

item='成绩'
if item in dt:
    dt.pop(item)
print(dt)

