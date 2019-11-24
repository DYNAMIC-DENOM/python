n=int(input("enter a number"))
sum=0
while n!=0:
    r=n%10
    sum=sum+r*r
    n=n//10
print("total squre value of these number seperetly",sum)