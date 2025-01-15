numbers = [1, 2, 3, 4, 5]

while True:
    indice = int(input("Entez l'indice que vous voulez remplacez (tappez  -1 pour sortir): "))
    if indice == -1:
        break
    if  indice>=0 and indice < len(numbers):
        value = int(input("Enterez votre valeur : "))
        numbers[indice] = value
        print(numbers)
    else:
        print("indice invalide. choisissez un autre.")