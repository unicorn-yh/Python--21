fo = open('name.txt','w+')
ls = ['0001','小明','1702班']
for line in ls:
    fo.writelines(line+'\n')
fo.seek(0)            #啥意思
for line in fo:
    print(line)
fo.close()