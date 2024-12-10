mot=str(input("entez votre mot: "))

verifpal=True


for i,j in enumerate(mot):
    if j!=mot[len(mot)-1-i]:
        verifpal=False
        break
        

if verifpal:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.") 