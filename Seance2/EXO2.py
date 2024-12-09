def temperaturetest(temperature):
    if temperature < 0 :
        print("It's freezing !!!")
    
    if temperature < 10 or temperature <0 :
        print("It's cold !!")  
    
    if temperature <20 :
        print("It's cool")
    
    if temperature > 39 :
        print("Extreme heat warning !!!!")
    
    print("Stay Safe")
        
#main
temperature= int(input("Entrée la température : "))
temperaturetest(temperature)