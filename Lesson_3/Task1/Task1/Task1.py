def sum(firstNumb, secondNumb):
    print("Sum of numbs - " + str(firstNumb + secondNumb))

def sub(firstNumb, secondNumb):
    print("Sub of numbs - " + str(firstNumb - secondNumb))

def mult(firstNumb, secondNumb):
    print("Mult of numbs - " + str(firstNumb * secondNumb))

def div(firstNumb, secondNumb):
    print("Division of numbs - " + str(firstNumb / secondNumb))

firstNumb = int(input("Enter first numb > "))
secondNumb = int(input("Enter second numb > "))
action = input("Action? (+, -, *, /) > ")

if(action == '+'):
    sum(firstNumb, secondNumb)

if(action == '-'):
    sub(firstNumb, secondNumb)

if(action == '*'):
    mult(firstNumb, secondNumb)

if(action == '/'):
    div(firstNumb, secondNumb)