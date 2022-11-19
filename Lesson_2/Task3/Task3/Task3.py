counter = int(input("Input size: "))
array = []

for numb in range(1, counter + 1):
    array.append(numb)

for numbs in range(0, counter):
    print(str(array))
    array.pop(-1)