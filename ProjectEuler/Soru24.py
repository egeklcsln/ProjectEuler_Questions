from itertools import permutations

digits="0123456789"

numbers= list(permutations(digits))
        
numberlist= numbers[999999] 
number=""
for i in numberlist:
    number= number + str(i)
    

print(number)
