
sum = 0  
count = 0  

for i in range(1, 101): 
    if i % 2 == 0:  
        sum += i
        count += 1

average = sum / count

print(average)