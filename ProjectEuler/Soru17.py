def letter(i):
    if i==0:
        return 0
    elif i==1 or i==2 or i==6 or i==10:
        return 3
    elif i==3 or i==7 or i==8:
        return 5
    elif i==4 or i==5 or i==9:
        return 4
    elif i==11 or i==12:
        return 6
    elif i==13 or i==14 or i==18 or i==19:
        return 8
    elif i==15 or i==16:
        return 7
    elif i==17:
        return 9
    elif (i>=20 and i<=39) or (i>=80 and i<=99):
        a=i%10
        return 6+letter(a)
    elif i>=40 and i<=69:
        a=i%10
        return 5 + letter(a)
    elif i>=70  and i<=79:
        a=i%10
        return 7 + letter(a)
    
    elif i%100==0 and i<1000:
        a= int(i/100)
        return letter(a) +7
    elif i>=100 and i<=999:
        a= int(i/100)
        b= i-a*100
        return letter(a)+10+letter(b)
    elif i==1000:
        return 11
  
sum =0
for i in range(1,1001):
    sum = sum + letter(i)