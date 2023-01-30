def fact(n):
    if n<=1:
        return 1
    
    return n*fact(n-1)

number = fact(100)
sum=0
for i in str(number):
    sum = sum + int(i)

print(sum)