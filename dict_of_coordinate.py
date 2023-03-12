#读取元数据
def DICTX(x):
    fr=open("D:/X.txt","r",encoding="UTF-8")
    lines=str(fr.readlines())
    lines=lines.replace("t","")
    lines=lines.replace("[","")
    lines=lines.replace("]","")
    lines=lines.replace("n","")
    lines=lines.replace("\\","")
    lines=lines.replace("'","")
    lines=lines.replace(" ,","")
    lines=lines.replace("","")
    #print(lines)
    list=lines.split(" ")
    #print(list)
    #print(len(list))
    dictX={}
    value=0
    for i in range(0,len(list)-1):
        if i%2==0:
            key=list[i];
        else:
            value=list[i];
        dictX[key]=value
    X=dictX.get(str(x))
    return float(X)
def DICTY(y):
    fr=open("D:/Y.txt","r",encoding="UTF-8")
    lines=str(fr.readlines())
    lines=lines.replace("t","")
    lines=lines.replace("[","")
    lines=lines.replace("]","")
    lines=lines.replace("n","")
    lines=lines.replace("\\","")
    lines=lines.replace("'","")
    lines=lines.replace(" ,","")
    lines=lines.replace("","")
    #print(lines)
    list=lines.split(" ")
    #print(list)
    #print(len(list))
    dictY={}
    value=0
    for i in range(0,len(list)-1):
        if i%2==0:
            key=list[i];
        else:
            value=list[i];
        dictY[key]=value
    Y = dictY.get(str(y))
    return float(Y)
def DICTZ(z):
    fr=open("D:/Z.txt","r",encoding="UTF-8")
    lines=str(fr.readlines())
    lines=lines.replace("t","")
    lines=lines.replace("[","")
    lines=lines.replace("]","")
    lines=lines.replace("n","")
    lines=lines.replace("\\","")
    lines=lines.replace("'","")
    lines=lines.replace(" ,","")
    lines=lines.replace("","")
    #print(lines)
    list=lines.split(" ")
    #print(list)
    #print(len(list))
    dictZ={}
    value=0
    for i in range(0,len(list)-1):
        if i%2==0:
            key=list[i];
        else:
            value=list[i];
        dictZ[key]=value
    Z = dictZ.get(str(z))
    return float(Z)



#print(DICTY(39))