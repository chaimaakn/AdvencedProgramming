
def remise(jours,nb,jour):
    if jour not in jours+["dimanche","samedi"]:
        print("jour invalide")
        return(-1)
    if jour in jours:
        remise=0.10
    elif jour not in jours:
        remise=0.20
        
    if nb > 5:
        remise = remise + 0.05
        
    return(remise)


#main
jours=["lundi","mardi","mercredi","jeudi","vendredi",]
montant=float(input("entrée votre montant: "))
nb=int(input("entrée le nb d'article: "))
jour=input("Entrée le jour: ").lower()
remise=remise(jours,nb,jour)
if remise != -1 :
  montant= montant - (remise*montant)
  print(f"Prix aprés remise: {montant:.2f} dinars")