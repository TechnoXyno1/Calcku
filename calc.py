#Making A Calc 

numberOne = int(input("[+] Enter Num\n"))
numberTwo = int(input("[+] Enter Num2\n"))

plus = int(input("[+] For + type 1\n For - type 2\n For x type 3 \n For / type 4\n"))
#Below One Is Invalid
#minus = int(input("[+] 2"))
#multiply = int(input("[+] 3"))
#division = int(input("[+] 4"))

if (plus == 1):
  print(numberOne + numberTwo)
elif (plus == 2):
  print(numberOne - numberTwo)
elif(plus == 3):
  print(numberOne * numberTwo)
elif(plus == 4):
  print(numberOne / numberTwo) 
else:
  print ("invalid")
