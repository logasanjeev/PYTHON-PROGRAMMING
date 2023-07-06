y= int(input("Enter No.of years of your service:"))
s= int(input("Enter your salary:"))
b=0
if(y>10):
    b= s/10
    print("Bonus= ",b)
elif(y>6 and y<10):
    b= 8*s/100
    print("Bonus= ",b)
else:
    b= 5*s/100
    print("Bonus= ",b)
