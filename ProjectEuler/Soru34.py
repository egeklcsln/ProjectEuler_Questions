def fact(x):
    
    if x==1 or x==0:
        return 1
    return x*fact(x-1)



max=fact(9)*7
total2=0
for i in range(3,max):
    total=0
    bas= str(i)
    for j in bas:
        total = total + fact(int(j))
    
    if total==i:
        total2=total2+ i
        
        
        
print(total2)  