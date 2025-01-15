Continue=True
while Continue:
    print("hi")
    response=input("Shall we continue ?").lower()
    if(response =='non'):
        Continue=False
    elif(response=='oui'):
        Continue=True
    else:
        print("la reponse doit etre oui ou non")
        
#python n'as pas de boucle do while python quand il rencontre le break il sort de la boucle et non pas du programme 