lisT = input("Enter string > ")

def listSort(lisT):
    print("Sort list > " + str(sorted(lisT)))

def wordCounter(lisT):
    print("Element in list > " + str(len(lisT)))

def vowconWords(lisT):
    vowels = 'AaEeIiOoUuYy'
    vowelsLetter = []
    consonantsLetter = []
    for letter in lisT:
        if letter in vowels:
            vowelsLetter.append(letter)
        elif (letter != ' '):
            consonantsLetter.append(letter)
    print("Vowels letter > " + str(vowelsLetter))
    print("Consonants letter > " + str(consonantsLetter))

def backWords(lisT):
    print(lisT.split()[::-1])

def indexWord(lisT):
    index = int(input("Enter index > "))
    if (index > len(lisT.split())):
        print("Incorrect index!")
    else:
        print("Word whis this index is " + lisT.split()[index - 1])

def swich(action, lisT):
    if (action == 1):
        listSort(lisT)

    if (action == 2):
        wordCounter(lisT)

    if (action == 3):
        vowconWords(lisT)

    if (action == 4):
        backWords(lisT)

    if (action == 5):
        indexWord(lisT)

    if (action == 6):
        print(lisT)

while(True):
    print("[1] List sort \n"
          "[2] Count element in list \n"
          "[3] Print vowels and consonants \n"
          "[4] Print list backwards \n"
          "[5] Word print by index \n"
          "[6] Print list \n"
          "[0] End program \n")
    action = int(input("Enter action > "))

    if (action == 0):
        break
    swich(action, lisT)

    print("===============================\n")
