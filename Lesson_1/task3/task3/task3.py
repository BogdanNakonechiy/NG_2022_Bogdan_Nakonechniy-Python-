userSecond = int(input("Enter sec > "))

sec = userSecond % 60
min = int((userSecond - sec) / 60)
hrs = int((min - min % 60) / 60)

print("\nDay > " + str(int(hrs / 24)) + " | Hrs > " + str(hrs % 24) + " | Min > " + str(min % 60) + " | Sec > " + str(sec) + "\n")