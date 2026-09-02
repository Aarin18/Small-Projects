def get_number(number):
     while True :
        operand1 = input ("Number   " + str ( number ) + ": ")
        try:
            return float(operand1)
            
        except:
            print("Invalide number , try again.")

operand1 = get_number(1)
operand2 = get_number(2)

sing = input("sing :")

valid = False
try :
     operand1 = float(operand1)
     operand2 = float(operand2)
     valid = True
except:
        print ("Invalide operands.")

if valid :
    result = 0
    if sing == "+":
        result = operand1 + operand2

    elif sing == "-":
        result = operand1 - operand2

    elif sing == "/":
        result = operand1 / operand2  
        if operand2 != 0:
            result = operand1 / operand2
        else:
            print("Division by zero. ")
                        
    elif sing == "*":
        result = operand1 * operand2

    else:
         print("Invalide sign.")

    print(result)

# i = 0
# while i <= 10:
#       print(i)
#       i += 2
#       break / continu
