
def pre():
    fr = open("D:/间隙水压.txt","r",encoding="UTF-8")
    fw = open("D:/间隙水压output.txt", "w", encoding="UTF-8")
    i=0
    new_list = []
    for i in fr:
        #print(i)
        i = str(i.strip())
        #print(type(i))
        list = i.split(" ")
        for j in list:
            if j !='':
                new_list.append(j)
        #print(new_list)
        new_list [1] = float(new_list[1])* 1000
        new_list[5] = float(new_list[5]) * 1000
        new_list[9] = float(new_list[9]) * 1000
        fw.write(new_list[0]+"  ")
        fw.write("{:.4E}".format(new_list[1])+"  ")
        fw.write(new_list[4]+"  ")
        fw.write("{:.4E}".format(new_list[5])+"  ")
        fw.write(new_list[8]+"  ")
        fw.write("{:.4E}".format(new_list[9])+'\n')
        new_list = []
    fr.close()
    fw.close()
pre()