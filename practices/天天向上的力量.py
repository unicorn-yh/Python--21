
def dayfunc(dayfac):
    power=1.0
    for i in range(365):
        if i%7 in [0,6]:
            power*=0.99  #power*=(1-dayfactor)
        else:
            power*=(1+dayfac)  #power*=(1+dayfactor)
    return power
dayfactor=0.01
while(dayfunc(dayfactor)<pow(1.01,365)):
    dayfactor+=0.001
print("工作日的力量：{:.2f}".format(dayfunc(dayfactor)))
print("工作日的努力参数是：{:.3f}".format(dayfactor))
