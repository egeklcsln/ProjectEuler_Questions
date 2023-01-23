def binary(x):
    return int((bin(x))[2:])


def isPalindromic(x):
    string=str(x)
    bool= True
    length = len(str(x))
    s=0
    for i in range(length-1,int(length/2)-1,-1):
        if string[i]!=string[s]:
                 bool=False
                 break
            
        if not bool:
            break
        s=s+1
    return bool

sum=0
for i in range(0,1000000):
    if isPalindromic(i) and isPalindromic(binary(i)):
        sum = sum+i