def div(n):
    sum =0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum = sum + i
            
            
    return sum
        




sum=0
for i in range (1,10001):
    if div(div(i))==i and i!=div(i):
        sum = sum + i
        
    
        
print(sum)