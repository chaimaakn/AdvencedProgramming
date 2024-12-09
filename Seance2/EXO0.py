nbtotal=int(input("entrez le nb de personnes : "))
capacitetaxi=int(input("entrez la capacite du taxi : "))

nbtaxi= nbtotal // capacitetaxi
if nbtotal % capacitetaxi > 0:
    nbtaxi+=1
    
print(f"nb taxi est : {nbtaxi}")
    
     
