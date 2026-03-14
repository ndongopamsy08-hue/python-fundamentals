# a user is going to select an arthmetic operation either addition subtraction mult and division
num1=int(input("enter any num1 value of your choice: "))
num2=int(input("enter any num2 value of your choice: "))
print("1)--addition\n\n")
print("2)--subtractionn\n")
print("3)--multiplictionn\n")
print("4)--divisionn\n")
choose=int(input("choose which operation you want to offer"))
if choose==1:
    result=num1+num2
    print(result)
elif choose==2:
    result=num1-num2
    print(result)
elif choose==3:
    result=num1*num2
    print(result)
elif choose == 4:
    result = num1 / num2
    print(result)
else:
    print("invalid operation")
    


