from dict_of_P import dict

fr = open("要素構成節点データ.txt","r",encoding="UTF-8")
fw = open("辺の间隙水压output.txt","w",encoding="UTF-8")
a = 8539
for i in fr:
    list = i.strip()
    list = list.split('\t')
    list = list[1:]
    for n in range(12):
        #print(list[j])
        if n < 7:
            reslut = (float(dict[list[n]])+float(dict[list[n+1]]))/2
            fw.write(str(a)+" ")
            fw.write("{:.4E}".format(reslut)+" ")
            if n == 2 or n == 5:
                fw.write("\n")
            a += 1
        elif n == 7:
            reslut = (float(dict[list[4]])+float(dict[list[7]]))/2
            fw.write(str(a) + " ")
            fw.write("{:.4E}".format(reslut)+" ")
            a += 1
        elif n == 8:
            reslut = (float(dict[list[0]])+float(dict[list[4]]))/2
            fw.write(str(a) + " ")
            fw.write("{:.4E}".format(reslut)+" ")
            fw.write("\n")
            a += 1
        elif n == 9:
            reslut = (float(dict[list[1]])+float(dict[list[5]]))/2
            fw.write(str(a) + " ")
            fw.write("{:.4E}".format(reslut)+" ")
            a += 1
        elif n == 10:
            reslut = (float(dict[list[2]])+float(dict[list[6]]))/2
            fw.write(str(a) + " ")
            fw.write("{:.4E}".format(reslut)+" ")
            a += 1
        elif n == 11:
            reslut = (float(dict[list[3]]) + float(dict[list[7]]))/2
            fw.write(str(a) + " ")
            fw.write("{:.4E}".format(reslut))
            fw.write("\n")
            a +=1