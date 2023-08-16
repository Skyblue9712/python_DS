print("enter any two numbers for performing arithmatic operation")
a=float(input())
b=float(input())
print("ENTERED VALUES : ")
print("a= ",a,"     b=",b)
print("ENTER THE FOLLOWING NUMBER FOR CORRESPONDING OPERATION:")
print("1:ADDITION")
print("2:SUBSTRACTION")
print("3:MULTIPLICATION")
print("4:DIVISION")
print("5:REMAINDER")
print("6:QUOTIENT")
print("7:EXPONENT")
op=int(input())
print(op)
co="c"
if op==1:
    print("Sum =",a+b)
    print("sarthak")

elif op==2:
    print("Substraction =",a-b)
elif op==3:
    print("Multiplication =",a*b)
elif op==4:
    print("Division=",a/b)
elif op==5:
    print("Remainder=",a%b)
elif op==6:
    print("Quotient=",a//b)
elif op==7:
    print("Exponent=",a**b)
else:  print("YOU HAVE ENTERED AN INCORRECT NUMBER")
c=" "
print("Enter c for continue")
