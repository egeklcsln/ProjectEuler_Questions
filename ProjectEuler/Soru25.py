n1=1
n2=1
n3=2
temp =0
s=3
while True:
    
   
   temp=n2
   n2=n3
   n1=temp
   n3= n1+n2
   s= s +1
   if len(str(n3))==1000:
       print(s)
       break