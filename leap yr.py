a=int(input("Enter the year  "))
b=a%4
c=a%100
if(c==0):
 print("This is not leap year")
elif(b==0):
  print("This year is leap year")
else:
  print("This is not leap year")
