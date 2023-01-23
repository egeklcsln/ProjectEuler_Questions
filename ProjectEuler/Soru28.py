sum=1
s=2
num=9
i=5
while not num>1001**2:
    a= num -s
    b= num -2*s
    c=num - 3*s
    sum = sum + a + b +c + num
    s=s+2
    num =i**2
    i= i +2
 
print(sum) 