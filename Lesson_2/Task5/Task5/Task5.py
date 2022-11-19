string = input("Enter string > ").split(",")
array = []

for numb in string:
    array.append(int(numb))

print("Max numb > " + str(max(array)))
print("Min numb > " + str(min(array)))

print("Sum array > " + str(sum(array)))
