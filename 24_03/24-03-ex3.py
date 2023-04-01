s = 0 

while (True):
    v = int(input("digite um numero a somar ou 0 para abrir: "))

    if(v == 0):
        break
    s = s + v
print("A soma é: ", s)