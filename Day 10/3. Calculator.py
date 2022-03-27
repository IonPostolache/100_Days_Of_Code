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

num1=int(input("What is the first number? "))

for k in operations.keys():
    print(k)
operation_symbol=input("Pick an operation from the line above: ")

num2=int(input("What is the second number? "))

answer_temp=operations[operation_symbol]
first_answer=answer_temp(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol=input("Pick another operation: ")
num3=int(input("What is the next number? "))
answer_temp=operations[operation_symbol]
second_answer=answer_temp(first_answer,num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


