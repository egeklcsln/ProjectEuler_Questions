sum=0
for i in range(2,1000000):
   
     a=int(i/100000)
     b=int(i/10000)%10
     c=int(i/1000)%10
     d=int(i/100)%10
     e=int(i/10)%10
     f=i%10      
           
     if i==(a**5 + b**5 + c**5 + d**5 + e**5+ f**5):
          sum= sum + i
    
print(sum)