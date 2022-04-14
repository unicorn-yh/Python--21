salary = eval(input())
if salary < 0:
    print('error')
elif 0 <= salary <= 5000:
    print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(0,salary))
else:
    if salary - 5000 <= 3000:
        tax= (salary-5000) * 0.03 - 0
        print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(tax,salary-tax))
    elif 3000 < salary - 5000 <= 12000:
        tax = (salary-5000) * 0.1 - 210
        print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(tax,salary-tax))
    elif 12000 < salary-5000 <= 25000:
        tax = (salary-5000) * 0.2 - 1410
        print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(tax,salary-tax))
    elif 25000 < salary-5000 <= 35000:
        tax = (salary-5000) * 0.25 - 2660
        print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(tax,salary-tax))
    elif 35000 < salary - 5000 <= 55000:
        tax = (salary-5000) * 0.3 - 4410
        print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(tax,salary-tax))
    elif 55000 < salary-5000 <= 80000:
        tax = (salary - 5000) * 0.35 - 7160
        print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(tax,salary-tax))
    elif salary - 5000 > 80000:
        tax = (salary-5000) * 0.45 - 15160
        print('应缴税款{:.2f}元，实发工资{:.2f}元。'.format(tax,salary-tax))


#2
def calTax(num):
    if num<=0:
        return 0
    elif num<=3000:
        return num*0.03
    elif num<=12000:
        return num*0.1-210
    elif num<=25000:
        return num*0.2-1410
    elif num<=35000:
        return num*0.25-2660
    elif num<=55000:
        return num*0.3-4410
    elif num<=80000:
        return num*0.35-7160
    else:
        return num*0.45-15160

salary = eval(input())
if salary<0:
    print("error")
else:
    delta = salary-5000
    print("应纳税{:.2f},，实发工资{:.2f}".format(calTax(delta), salary-calTax(delta)))
    
