list1=[1,3,2,6,4,7,7,3]
uniq=[]
for i in list1:
    if i not in uniq:
        uniq.append(i)
print(uniq)
