a= int(input("Enter the first side of the triangle:"))
b= int(input("Enter the second side of the triangle:"))
c= int(input("Enter the third side of the triangle:"))
if(a+b>c and b+c>a and a+c>b):
    print("Triangle is possible")
else:
    print("Triangle is not possible")
