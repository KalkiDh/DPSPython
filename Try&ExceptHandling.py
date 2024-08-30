try:
    num1=int(input("Enter a number : "))
    num2=int(input("Enter a number : "))

    sum=num1+num2
    print("Sum of the nos. are : ",sum)
except Exception as dron :
    print(dron)
print("This line needs to be printed any how")