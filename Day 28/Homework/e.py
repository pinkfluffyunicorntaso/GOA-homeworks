
pos = 0
neg = 0

for i in range(5):
    num = int(input("pls put in a number"))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print(pos)
print(neg)