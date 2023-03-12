import dict_of_coordinate
def sum(a,b):
    result = ((a+b)/2)
    return result
def keisan():
    #with open("D:/test.txt","r",encoding="UTF-8")as fr_input:
        #print(fr_input)
    fr_o = open("D:/要素構成節点データ.txt", "r", encoding="UTF-8")
    fw_data = open("D:/dataoutput.txt", "w", encoding="UTF-8")
    #with open('D:/test1.csv', newline='',encoding="utf-8-sig") as f:
        #reader = csv.reader(f)
        #data = [row for row in reader]
    #print(type(data))
    j = 8538
    line=[]
    for x in fr_o:
        list=x.split()
        intlist=[int(j) for j in list]
        #print(intlist)
        #print(intlist[1])
        #print(intlist[2])
        for i in range(1,13):
            j = j + 1
            if i < 8:
                result_x = sum(dict_of_coordinate.DICTX(intlist[i]), dict_of_coordinate.DICTX(intlist[i+1]))
                result_y = sum(dict_of_coordinate.DICTY(intlist[i]), dict_of_coordinate.DICTY(intlist[i+1]))
                result_z = sum(dict_of_coordinate.DICTZ(intlist[i]), dict_of_coordinate.DICTZ(intlist[i+1]))
                print(j,result_x,result_y,result_z)
                line = str(j)+'   '
                fw_data.write(line)
                fw_data.write(str(result_x) + '   ')
                fw_data.write(str(result_y) + '   ')
                fw_data.write(str(result_z) + '   ')
                fw_data.write("\n")
            else:
                if i == 8:
                    result_x = sum(dict_of_coordinate.DICTX(intlist[5]), dict_of_coordinate.DICTX(intlist[8]))
                    result_y = sum(dict_of_coordinate.DICTY(intlist[5]), dict_of_coordinate.DICTY(intlist[8]))
                    result_z = sum(dict_of_coordinate.DICTZ(intlist[5]), dict_of_coordinate.DICTZ(intlist[8]))
                    print(j, result_x, result_y, result_z)
                    line = str(j)+'   '
                    fw_data.write(line)
                    fw_data.write(str(result_x)+'   ')
                    fw_data.write(str(result_y)+'   ')
                    fw_data.write(str(result_z)+'   ')
                    fw_data.write("\n")
                if i == 9:
                    result_x = sum(dict_of_coordinate.DICTX(intlist[1]), dict_of_coordinate.DICTX(intlist[5]))
                    result_y = sum(dict_of_coordinate.DICTY(intlist[1]), dict_of_coordinate.DICTY(intlist[5]))
                    result_z = sum(dict_of_coordinate.DICTZ(intlist[1]), dict_of_coordinate.DICTZ(intlist[5]))
                    print(j, result_x, result_y, result_z)
                    line = str(j)+'   '
                    fw_data.write(line)
                    fw_data.write(str(result_x)+'   ')
                    fw_data.write(str(result_y)+'   ')
                    fw_data.write(str(result_z)+'   ')
                    fw_data.write("\n")
                if i == 10:
                    result_x = sum(dict_of_coordinate.DICTX(intlist[2]), dict_of_coordinate.DICTX(intlist[6]))
                    result_y = sum(dict_of_coordinate.DICTY(intlist[2]), dict_of_coordinate.DICTY(intlist[6]))
                    result_z = sum(dict_of_coordinate.DICTZ(intlist[2]), dict_of_coordinate.DICTZ(intlist[6]))
                    print(j, result_x, result_y, result_z)
                    line = str(j)+'   '
                    fw_data.write(line)
                    fw_data.write(str(result_x)+'   ')
                    fw_data.write(str(result_y)+'   ')
                    fw_data.write(str(result_z)+'   ')
                    fw_data.write("\n")
                if i == 11:
                    result_x = sum(dict_of_coordinate.DICTX(intlist[3]), dict_of_coordinate.DICTX(intlist[7]))
                    result_y = sum(dict_of_coordinate.DICTY(intlist[3]), dict_of_coordinate.DICTY(intlist[7]))
                    result_z = sum(dict_of_coordinate.DICTZ(intlist[3]), dict_of_coordinate.DICTZ(intlist[7]))
                    print(j, result_x, result_y, result_z)
                    line = str(j)+'   '
                    fw_data.write(line)
                    fw_data.write(str(result_x)+'   ')
                    fw_data.write(str(result_y)+'   ')
                    fw_data.write(str(result_z)+'   ')
                    fw_data.write("\n")
                if i == 12:
                    result_x = sum(dict_of_coordinate.DICTX(intlist[4]), dict_of_coordinate.DICTX(intlist[8]))
                    result_y = sum(dict_of_coordinate.DICTY(intlist[4]), dict_of_coordinate.DICTY(intlist[8]))
                    result_z = sum(dict_of_coordinate.DICTZ(intlist[4]), dict_of_coordinate.DICTZ(intlist[8]))
                    print(j, result_x, result_y, result_z)
                    line = str(j)+'   '
                    fw_data.write(line)
                    fw_data.write(str(result_x)+'   ')
                    fw_data.write(str(result_y)+'   ')
                    fw_data.write(str(result_z)+'   ')
                    fw_data.write("\n")
        print('-------------------')
    fr_o.close()
    fw_data.close()
keisan()