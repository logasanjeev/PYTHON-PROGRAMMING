y= int(input("Enter the year: "))
if(y%400==0):
    print(y," is a leap year")
elif(y/400!=1 and y%100==0):
    print(y," is a leap year")
elif(y/400!=1 and y%100!=0 and y%4==0):
    print(y," is a leap year")
else:
    print(y," is not a leap year")
