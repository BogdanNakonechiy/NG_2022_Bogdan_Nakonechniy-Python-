string = input("Enter string > ").split(",")
array = []

for i in string:
    array.append(int(i))

print("Max numb > " + str(max(array)))
print("Min numb > " + str(min(array)))

print("Sum array > " + str(sum(array)))
