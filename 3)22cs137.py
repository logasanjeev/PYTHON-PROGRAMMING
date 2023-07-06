t= int(input("Enter the temperature:"))
v= int(input("Enter the speed of wind:"))
wc= 13.12*0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
print("The wind chill index:",wc)
