def calculator(num1 , op ,num2 ):
    if op =="+":
        return num1 + num2
    elif op =="-":
        return num1 - num2
    elif op =="*":
        return num1 * num2
    elif op =="/":
        return num1 / num2
    else:
        return "Invalid Operation"
while True:
    num1= input("Enter First Number : ")
    if num1.lower() =="exit":
        break
    op=input("Enter Operation Type(+, -, *, /) : ")
    num2 = input("Enter Second Number : ")

    result = calculator(int(num1),op,int(num2))
    print("Answer : {a}".format(a=result))
