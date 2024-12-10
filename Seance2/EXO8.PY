print("entrée:")
number=int(input("Number:"))
print("sortie:")
if(number%3==0):
    print("Fizz")
elif(number%5==0):
    print("Buzz")
elif(number%3==0 and number%5==0):
    print("FizzBuzz")