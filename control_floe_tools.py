# -*- coding: utf-8 -*-
"""control floe tools

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/131RcmvS5Gyo0rG9JcaBt6cEcJU6DArUz
"""



"""Control Flow and **Loops

if statemet
"""

age=18
if age>=18:
  print("youare egeible to vote")

num=int(input("enter a number"))
if num%2==0:
  print("number is even")
else:
    print("odd number")

marks=int(input("enter your marks:"))
if marks>=90:
  print ("grade:A")
elif marks>=75:
   print("grade:B")
else:
   print("grade: F")

for i in range(5):
  print("interation",i)

for i in range(5,10,5):
  print("iteration:",i)

"""while loop"""

count=0
while count<5:
  print("count:",count)
  count+=1



"""control floe tools   
break
"""

for i in range(10):
  if i ==5:
    break
  print(i)



"""continue"""

for i in range(10):
  if i==5:
    continue
  print(i)

"""pass"""

for i in range(5):
  if i ==5:
    pass
    else
