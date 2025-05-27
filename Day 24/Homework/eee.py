
secret = 4
cda = 3

while cda > 0:
    user_ricxvi = int(input("guess the secret num "))
    cda -= 1
    if user_ricxvi == secret:
        print("yayyyy you guessed it!!!")
        break
    elif cda == 0:
        print("awhh sorry you lost you get five big booms 🤣🤣🤣")