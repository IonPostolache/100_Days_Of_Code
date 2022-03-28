from art import logo
#Add
def add(n1,n2):
    return n1+n2
#Subtract
def subtract(n1,n2):
    return n1-n2
#Multiply
def multiply(n1,n2):
    return n1*n2
#Divide
def divide(n1,n2):
    return n1/n2

operations={"+":add,"-":subtract, "*":multiply, "/":divide}

def calculation():
    print(logo)
    num1=float(input("What is the first number? "))
    for k in operations.keys():
        print(k)

    continuation="y"
    while continuation!="n":
        operation_symbol=input("Pick an operation: ")
        num3=float(input("What is the next number? "))
        answer_temp=operations[operation_symbol]
        second_answer=answer_temp(num1,num3)
        print(f"{num1} {operation_symbol} {num3} = {second_answer}")
        continuation = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to exit.")
        num1=second_answer
        if continuation=="n":
            calculation()

calculation()




