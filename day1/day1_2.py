file1 = open("/home/valentin/Documentos/AdventOfCode24/day1/inputD1.txt", "r")

list1 = []
list2 = []
while True:
    line = file1.readline()
    if not line: break
    separate = line.split(" ")
    list1.append(int(separate.pop(0)))
    temp = separate.pop(2)
    temp.rstrip()
    list2.append(int(temp))

#ya estan las listas separadas, falta operar
index1 = 0
index2 = 0
suma = 0
while index1 < len(list1):
    while index2 < len(list2):
        if(list1[index1] == list2[index2]):
            suma = suma + list1[index1]
        index2 += 1
    index1 += 1
    index2 = 0

print(suma)
file1.close