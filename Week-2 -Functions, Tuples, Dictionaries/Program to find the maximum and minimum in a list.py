list1=list(map(int,input("Enter a list of numbers").split()))
print(list1)
print("THe max is ",max(list1))
print("THe min is ",min(list1))
#this is another way to solve this
list1.sort()
print("THe maximum is ",list1[-1],"\n The Minimum is ",list1[0])
