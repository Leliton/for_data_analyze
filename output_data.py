



f = open("D:/data1.txt", "w",encoding="UTF-8")
j=8527
for line in range(1,6939):
    for i in range(1,13):
        j=j+1
        if i<12:
            f.write(str(j)+" " )
        else:
            f.write(str(j)+"\n")



f.close()
