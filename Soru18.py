list =[]
with open("ucgen.txt", "r",encoding='utf8') as dosya:
  for satir in dosya:
      txt = satir.split()
      list.append(txt)
  
for i in range (0,len(list)):
    for j in range(0,len(list[i])):
        list[i][j]=int(list[i][j])
        
    
    

    
for i in range(len(list)-1,-1,-1):
    for j in range(0,i):
        list[i-1][j] = list[i-1][j] + max(list[i][j],list[i][j+1])

                                                        
print(list[0])   