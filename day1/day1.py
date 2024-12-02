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

list1.sort()
list2.sort()

index = 0
suma = 0

while index < len(list1):
    suma = suma + abs(list1[index] - list2[index])
    index += 1

print(suma)

file1.close