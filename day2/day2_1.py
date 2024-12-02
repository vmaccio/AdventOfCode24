file1 = open("/home/valentin/Documentos/AdventOfCode24/day2/inputD2.txt", "r")

suma = 0

while True:
    line = file1.readline()
    if not line: break
    separate = line.split(" ")

    index = 2
    previo = int(separate[0])
    siguiente = int(separate[1])
    if (previo > siguiente and abs(previo-siguiente) <= 3):
        while index < len(separate):
            previo = siguiente
            siguiente = int(separate[index])
            if(previo > siguiente and abs(previo-siguiente) <= 3):
                if(index + 1 == len(separate)):
                    suma += 1
            else:
                break
            index += 1
    elif (previo < siguiente and abs(previo-siguiente) <= 3):
        while index < len(separate):
            previo = siguiente
            siguiente = int(separate[index])
            if(previo < siguiente and abs(previo-siguiente) <= 3):
                if(index + 1 == len(separate)):
                    suma += 1
            else:
                break
            index += 1
        

print(suma)

file1.close