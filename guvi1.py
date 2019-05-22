a=int(input(" enter the starting kilometer  "))
b=int(input(" enter the ending  kilometer "))
if((a>=0)&(a<b)):
  c=b-a
  print(" 1.Auto ")
  print(" 2.indico ")
  print(" 3.innova ")
  print(" 4.BMW ")
  d=int(input(" your cab name "))
  if (d==1):
   c=c*7
  elif(d==2):
   c=c*9
  elif(d==3):
   c=c*12
  elif(d==4):
    c=c*20
  else:
   print(" Enter the correct option")
  print("Thankyou for your jurnny")
  print ("you travell from "+str(a) +"Km   to   "+str(b)+"Km ")
  print("your travelling charge is :  "+str(c)+"Rs ")
else:
  print(" Enter the correct starting & ending Km")

