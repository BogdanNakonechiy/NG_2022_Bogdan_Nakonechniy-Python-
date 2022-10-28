numbA = float(input("Enter first numb >> "))
numbB = float(input("Enter srcond numb >> "))
action = input("Select action (+, -, *, /) > ")

print("\nResult ")
if(action == '+'):
    print(numbA + numbB)
if(action == '-'):
    print(numbA - numbB)
if(action == '*'):
    print(numbA * numbB)
if(action == '/'):
    print(numbA / numbB)