def main():
    fr = open("D:/辺の要素構成節点データ.txt","r",encoding="UTF-8")
    fw = open("D:/辺の要素構成節点データoutput.txt", "w", encoding="UTF-8")
    i=0
    for i in fr:
        #print(i)
        i = str(i.strip())
        #print(type(i))
        list=i.split(" ")
        for j in range(0,len(list)):
            #print(list[j])
            fw.write(list[j]+"\n")
    fr.close()
    fw.close()
main()