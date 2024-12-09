def diffage(agepersone,ageperstwo):
    if(agepersone or ageperstwo)<=0 :
        print("Age invalide il doit etre > 0")
        return(-1)
    if(agepersone > ageperstwo):
        return(agepersone)
    elif (agepersone < ageperstwo):
        return(ageperstwo)
    
    return(0)


#main
persone=int(input("entrer age personne 1: "))
perstwo=int(input("entrer age personne 2: "))

age=diffage(persone,perstwo)
if(age !=-1):
  if(age==0 ):
    print("les deux ont le méme age")
  else:
    print(f"le plus grand age est : {age}")