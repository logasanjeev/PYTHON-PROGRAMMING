f= int(input("Food rating(1-5):"))
s= int(input("Service rating(1-5):"))
a= int(input("Ambience rating(1-5):"))
am=int(input("Bill's Amount:"))
if(f==4 or f==5):
    if(s==4 or s==5 and a==4 or a==5):
        print("tip= ",am*10/100)
    elif(s==1 or s==2 or s==3 and a==1 or a==2 or a==3):
        print("tip= ",am*5/100)
elif(f==1 or f==2 or f==3):
    if(s==4 or s==5 and a==4 or a==5):
        print("tip= ",am*5/100)
    elif(s==1 or s==2 or s==3 and a==1 or a==2 or a==3):
        print("tip= ",am*1/100)
else:
    print("Enter valid data")
    
    

        
