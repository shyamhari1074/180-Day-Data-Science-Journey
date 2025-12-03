n =int(input("Enter the number: "))
print("The fibonacci sequence is")
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

