
weli = int(input("put in a year"))

if weli % 4 == 0 and weli % 100 != 0 or weli % 400 == 0:
    print("nakiania")
else:
    print("ar aris nakiani")