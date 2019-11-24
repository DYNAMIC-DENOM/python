text=input("write something")
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
for letter in text:
    if letter=="a"or  letter=="A":
        a_count=a_count+1
    if letter=="e" or  letter=="E":
        e_count=e_count+1
    if letter=="i" or  letter=="I":
        i_count=i_count+1    
    if letter=="o" or  letter=="O":
        o_count=o_count+1
    if letter=="u" or  letter=="U":
        u_count=u_count+1
print("A", a_count)
print("E", e_count)   
print("I", i_count)   
print("O", o_count)   
print("U", u_count)                