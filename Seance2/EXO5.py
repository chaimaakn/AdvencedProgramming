def difftime(time1,time2):
    if(time1 or time2) < 0:
        print("Temps invalide")
        return(-1)
    else:
        if(time1 > time2):
            return(1)
        elif time1 < time2:
            return(2)
        return(0)
    
#main
print("Runner 1")
Name1=input("Name1: ")
time1=float(input("time1: "))
print("Runner 2")
Name2=input("Name2: ")
time2=float(input("time2: "))
vainceur=difftime(time1,time2)
if(vainceur != -1):
    if(vainceur==1):
        print(f"le plus rapide est : {Name2}")
    elif(vainceur==2):    
        print(f"le plus rapide est : {Name1}")
    else:
        print("ils ont le meme temps")    