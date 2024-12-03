import re

file1 = open("/home/valentin/Documentos/AdventOfCode24/day3/inputD3.txt", "r")

suma = 0

text = file1.read()

afterRex = re.findall("mul\([0-9]*,[0-9]*\)",text)
#print(afterRex)

index = 0
while index < len(afterRex):
    mul = re.findall(("[0-9]*"), afterRex[index])
    suma = suma + (int(mul[4]) * int(mul[6]))
    index += 1

print(suma)

file1.close