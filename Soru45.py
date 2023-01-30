def triangle(x):
    
    return int((x*(x+1))/2)
        
def pentagonal(x):
    
    return int((x*(3*x-1))/2)

def hexagonal(x):
    
    return (x*(2*x-1))
    
 
t=286
p=166
h=144

while True:
    bool1=False
    bool2=False
    result=triangle(t)
    
    
    while True:
        
        if pentagonal(p)==result:
            bool1=True
            break
        if pentagonal(p)>result:
            break
        p=p+1
        
        
    while True:
        
        if hexagonal(h)==result:
            bool2=True
            break
        if hexagonal(h)>result:
            break
        h=h+1
        
        
        
    if bool1 and bool2:
        print(result)
        break
    t=t+1