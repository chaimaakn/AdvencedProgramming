from math import sqrt


Juste=True
while Juste:
   number=int(input("enter an integer number "))
   if(number<0):
      print("invalid number")
   elif(number >0):
       print(f"{sqrt(number):.2f}")
   else:
       break        