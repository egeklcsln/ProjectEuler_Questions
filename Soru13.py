list=[]

with open("numbers.txt", "r",encoding='utf8') as file:
  
  for l in file:
      txt = l.split()
      txt = txt[0]
      list.append(txt)
      
      
      
  sum=0
  for number in list:
      sum = sum+ int(number)



result = int(sum/(10**42))
print(result)