n= int(input())
c=0
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i%j==0):
            c=c+1
        if(c==2):
            print(i,end=',')
        else:
            continue;
        

        

        
    
