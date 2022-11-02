array = input("Enter str > ")
counter = {}

for letter in array:
    if letter in counter:
        counter[letter] += 1
    else:
        counter.update({letter : 1})

for k, v in counter.items():
  print(k + " - " + str(v))

