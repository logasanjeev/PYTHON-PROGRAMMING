a= int(input())
b= int(input())
c=0
for i in range(a,b+1,1):
    for j in range(a,b+1,1):
        if(i%j==0):
            c=c+1
            
    
