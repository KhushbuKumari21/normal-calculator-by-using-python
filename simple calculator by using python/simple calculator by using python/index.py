num1 = int(input("Enter the value 1 : "))
num2 = int(input("Enter the value 2 :"))
opr = input("Enter the operator")
if opr == "+":
    print (num1 + num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else :
    print("Invalid operator")
