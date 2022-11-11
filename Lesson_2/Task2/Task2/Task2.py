string = input("Enter > ")

for i in string:
    if i not in array:
        array.append(i)

print("\nArray > " + str(array.split()))
