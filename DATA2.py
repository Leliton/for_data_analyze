fr = open("D:/X.txt", "r", encoding="UTF-8")
lines = str(fr.readlines())
lines = lines.replace("t", "")
lines = lines.replace("[", "")
lines = lines.replace("]", "")
lines = lines.replace("n", "")
lines = lines.replace("\\", "")
lines = lines.replace("'", "")
lines = lines.replace(" ,", "")
lines = lines.replace("", "")
# print(lines)
list = lines.split(" ")
# print(list)
# print(len(list))
dictX = {}
value = 0
for i in range(0, len(list) - 1):
    if i % 2 == 0:
        key = list[i];
    else:
        value = list[i];
    dictX[key] = value
X = dictX.get(key)
print(X)


