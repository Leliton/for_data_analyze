

fr = open("D:/辺の间隙水压.txt", "r", encoding="UTF-8")
list_key = []
list_value = []
dict = {}
for i in fr:
    i = str(i.strip())
    # print(type(i))
    list = i.split("  ")
    for j in list:
        if len(j) < 5:
            list_key.append(j)
        else:
            list_value.append(j)
dict = {k:v for k,v in zip(list_key,list_value)}
