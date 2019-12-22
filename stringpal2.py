x="malayalam"
print(x[0:3])
print(x[:3])
print(x[::2])
print(x[0:10:2])
print(x[::-1])
if x==x[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
r=""
for i in x:  
    r=i+r
    print(r)
