print("---------------------------")
print("--------BIENVENIDO---------")
print("---------------------------")

N = int(input("digite el valor que deseas invertir: "))

## proceso

N1 = N%10
N2 = N//10
N3 = N2%10
N4 = N2//10

A = N1*100
B = N3*10
C = N4*1

NI = A+B+C


print("este es el numero inverso: " + str(NI))