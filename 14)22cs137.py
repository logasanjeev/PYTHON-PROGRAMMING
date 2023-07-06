s= int(input("Start: "))
e= int(input("End: "))
ev=0
od=0
for i in range(s,e+1,1):
    if(i%2==0):
        ev=ev+1
    else:
        od=od+1
print("Even : ",ev)
print("Odd : ",od)

    
