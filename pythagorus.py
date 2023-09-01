a=int(input("Enter the value of first side :"))
b=int(input("Enter the value of second side:"))
c=input("Enter the side which you want to find :")
ans=0
match c:
    case "H":
        ans=(a**2+b**2)**0.5
        print(f"The value of Hypotenous is {ans}")
    case "B":
     if b>a:
         ans=(b**2-a**2)**0.5
         print(f"The value of Base is {ans}")
     else:
         ans=(a**2-b**2)**0.5
         print(f"The value of Base is {ans}")
    case "P":
       if b>a:
         ans=(b**2-a**2)**0.5
         print(f"The value of Perpendicular is {ans}")
       else:
         ans=(a**2-b**2)**0.5
         print(f"The value of Perpendicular is {ans}")
         
    case _:
        print("Invalid Input")