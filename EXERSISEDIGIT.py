digit=int(input("enter a number "))
def countofdigit(digit):
    count=0
    while digit!=0:
         digit=digit//10
         count=count+1
    print("Your input carries",count,"digits")
countofdigit(digit)
def sumofdigit(digit):
    sum=0
    while digit!=0:
         r=digit%10
         sum=sum+r
         digit=digit//10
    print("The sum of your input is",sum)
sumofdigit(digit)
def reverseofdigit(digit):
    reverse=0
    while digit!=0:
         r=digit%10
         reverse=reverse*10+r
         digit=digit//10
    # print("The reverse of your input is",reverse)
    return reverse
x=reverseofdigit(digit)
print("The reverse of your number is",x)
def palindrome(digit):
    if reverseofdigit(digit)==digit:
        print("This is a palindrome number")
    else:
        print("This is not a palindrome number")
palindrome(digit)
    


         