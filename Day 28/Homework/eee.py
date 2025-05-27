
num = int(input("put in a number "))
if num <= 1:
    print("ar aris martivi")
else:
    for i in range(2, num):
        if num % i == 0:
            print("ar aris martivi")  
            break
    else:
        print("martivia") 
