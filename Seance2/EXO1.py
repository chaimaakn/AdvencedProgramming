name=input("entrez votre nom : ")
if(name == "VIP"):
    print("Enjoy the show for free!")
else:
    nbticket=int(input("entrez le nombre de ticket que vous voulez : "))
    prix=nbticket*15.50
    print(f"le prix totale est {prix}\nEnjoy your tickets")
    