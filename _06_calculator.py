from email.policy import default

num1 = input("Enter num1 value : ")
num2 = input("Enter num2 value : ")

Operator = input("Enter the operator : ")

match Operator :
 case "+":
    print(int(num1)+int(num2))
 case"-":
    print(int(num1)-int(num2))
 case"*":
    print(int(num1)*int(num2))
 case"/":
    print(int(num1)/int(num2))
 case"%":
  print(int(num1)%int(num2))
default 
print(" Sorry! its an wrong operator ")

