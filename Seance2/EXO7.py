def checkleap(year):
    
  if(year%4==0):
    print("That year is a leap year.")
  elif(year%100==0 and year%400==0):
     print("That year is a leap year.")
  else:
     print("That year is not  a leap year.")





#main
year=int(input("Please type in a year:"))
checkleap(year)

