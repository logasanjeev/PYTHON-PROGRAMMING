n= input("Enter your name:")
a= int(input("Enter your age:"))
g= input("Enter you gender (M/F):")
d= int(input("Enter No.of days:"))
if(a>=18 and a<30 and g=='M'):
    print("Amount to be paid= ",700*d)
elif(a>=18 and a<30 and g=='F'):
    print("Amount to be paid= ",750*d)
elif(a>=30 and a<=40 and g=='M'):
    print("Amount to be paid= ",800*d)
elif(a>=30 and a<=40 and g=='F'):
    print("Amount to be paid= ",800*d)
else:
    print("Enter valid data and try again!!")

