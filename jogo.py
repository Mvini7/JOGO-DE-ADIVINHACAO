print("Tente sair da masmorra!")

lista = []

for i in range(10, 31):

    if i % 2 > 0:
        lista.append(i)

print(lista)
print("Esses são os numeros primos entre 10 e 30!")
print("Um desses numeros te liberta da masmorra!")

while True:

    numeros = input("Digite um numero entre 10 e 30 que seja primo para sair da masmorra: ")

    try:
        numeros = int(numeros)

        if numeros == 21:
            print("Você estar livre da masmorra!")
            break
        elif numeros not in lista:
            print("Esse numero não é primo!")
    except ValueError:
        print("Digite um numero valido!")
