sum=0
for i in range(1,1001):
    sum = sum + i**i
    
    
result=str(sum)
result= result[len(result)-10:]
print(result)    