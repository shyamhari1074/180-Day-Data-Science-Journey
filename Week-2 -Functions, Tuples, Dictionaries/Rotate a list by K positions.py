lst=[1,2,3,4,5,6,7,8,9]
k=3
for _ in range(k):
    last=lst.pop()
    lst.insert(0,last)
print(lst)
#another method
lst1=[1,2,3,4,5,6,7,8,9]
k=k%len(lst)
rot=lst1[-k:]+lst1[:-k]
print(rot)
