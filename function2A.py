name=input("enter your name ")
def greeting(n):
    print("hi,",name+".")
greeting(name)
greeting("DJM")

gender=input("enter 'f' for female & 'm' for male ")
def chromosome(gender):
    if gender=='m':
        print(name,"-",'you might have XY type chromosome')
    elif gender=='f':
        print(name,"-",'you might have XX type chromosome')
    else:
        print(name,"-",'you might have SONAI NANDI type chromosome')
chromosome(gender)

