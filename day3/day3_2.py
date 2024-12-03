file1 = open("/home/valentin/Documentos/AdventOfCode24/day3/inputD3.txt", "r")

suma = 0

def legalOrNot(entrada):
    #print(entrada)
    legal = 0;
    index = 2
    previo = int(entrada[0])
    siguiente = int(entrada[1])
    if (previo > siguiente and abs(previo-siguiente) <= 3):
        while index < len(entrada):
            previo = siguiente
            siguiente = int(entrada[index])
            if(previo > siguiente and abs(previo-siguiente) <= 3):
                if(index + 1 == len(entrada)):
                    legal += 1
            else:
                return index
            index += 1
    elif (previo < siguiente and abs(previo-siguiente) <= 3):
        while index < len(entrada):
            previo = siguiente
            siguiente = int(entrada[index])
            if(previo < siguiente and abs(previo-siguiente) <= 3):
                if(index + 1 == len(entrada)):
                    legal += 1
            else:
                return index
            index += 1
    else:
        return index
    if(legal > 0):
        return -1
    else:
        return 0

while True:
    line = file1.readline()
    if not line: break
    separate = line.split(" ")

    temp = legalOrNot(separate)
    if (temp == -1):
        suma += 1
    else:
        copy1 = separate.copy()
        copy2 = separate.copy()
        copy3 = separate.copy()
        copy1.pop(temp)
        #print(copy1)
        copy2.pop(temp - 1)
        #print(copy2)
        copy3.pop(temp - 2)
        #print(copy3)
        if (legalOrNot(copy1) == -1 or legalOrNot(copy2) == -1 or legalOrNot(copy3) == -1):
            suma += 1


print(suma) #802 too high, 468 too low. 476 just perfect

file1.close