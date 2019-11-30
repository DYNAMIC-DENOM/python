input1=int(input("enter a number "))
input2=int(input("enter a number "))
operator=input("choose any one of thse symbol + - * / __ ")
def calculator(n1,n2,op):
    if op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="*":
        print(n1*n2)
    elif op=="/":
        print(n1/n2)
    else:
        print("this is a wrong input")
calculator(input1,input2,operator)
