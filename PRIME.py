num=int(input("enter a number"))
is_P=True
for i in range(2,num):
    if num%i==0:
        # print(num,"is a nonprime number")
        is_P=False
        break
if is_P==True:
    print(num,"is a prime number")
else:
    print(num,"is a nonprime number")


