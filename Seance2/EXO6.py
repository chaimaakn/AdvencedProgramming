def sep(montant):
    dinards=int(montant)
    centimes=round((montant - dinards)*100)
    return(dinards,centimes)


#main
montant=float(input("entrez le montant: "))
(dinards,centimes)=sep(montant)

print(f"dinards:{dinards} \ncentimes:{centimes}")