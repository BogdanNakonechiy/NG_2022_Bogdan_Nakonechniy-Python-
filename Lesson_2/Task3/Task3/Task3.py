counter = int(input("Input size: "))
array = []

for i in range(1, counter + 1):
    array.append(i)

for i in range(0, counter):
    print(str(array))
    array.pop(-1)