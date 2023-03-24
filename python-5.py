'''Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:'''

import time
time_rightnow= int(time.strftime("%H"))
print(time_rightnow)

if time_rightnow >=1 and time_rightnow<=12:
  print("GOODMORNING SIR")
elif time_rightnow>=12 and time_rightnow<=4:
  print("GOODAFTERNOON SIR")
elif time_rightnow>=4 and time_rightnow<=8:
  print("GOODEVENING SIR")
else:
  print("GOODNIGHT SIR")

'''Given an integer,n, perform the following conditional actions:
1. If n is odd, print (Weird)
2. If n is even and in the inclusive range of 2 to 5, print       (Not Weird)
3. If n is even and in the inclusive range of 6 to 20,print       (Weird)
4. If n is even and greater than 20, print (Not Weird).'''

n=int(input())

if n%2==0 and n>=2 and n<=5:
    print("Not Weird")
elif n%2==0 and n>=6 and n<=20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")
else:
    print("Weird")

  

