number=int(input("plesae enter apositive integer number"))
operande1=1
operande2=1
while True:
    rslt=(operande1*operande2)
    print(f"{operande1}*{operande2}={rslt}")
    if(operande1 > number):
        operande1=1
        operande2=operande2+1 
    elif(operande2<9):
        operande2=operande2+1
    else:
        operande1=operande1+1
        operande2=1        