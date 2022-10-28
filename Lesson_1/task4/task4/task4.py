a = int(input("Enter A > "))
b = int(input("Enter B > "))
c = int(input("Enter C > "))

D = b * b - 4 * a * c

if(D < 0):
    print("\nNo roots found\n")

if(D == 0):
    print("\nX = " + str(-(b/ (2 * a))) + "\n")

if(D > 0):
    print("\nX1 = " + str(-b + (D/D)/(2*a)))
    print("X2 = " + str(-b - (D/D)/(2*a)) + "\n")