
atimeti = 0
atinaklebi = 0


for i in range(3):
    num = int(input("put in a number"))
    if num > 10:
        atimeti += 1
    elif num <= 10:
        atinaklebi += 1

if atimeti == 3:
    print("all numbers are greater than 10")
elif atimeti != 3:
    print("Some numbers are less than or equal to ten.")