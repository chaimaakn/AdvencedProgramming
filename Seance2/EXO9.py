print("entrez les noms des cités. Tapez 'stop' pour terminer")

while True:
    citenom=input("entrez le nom la cité")
    if(citenom.lower() == "stop"):
        break
    elif citenom:
        population