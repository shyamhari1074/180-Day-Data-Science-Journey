def freq(list1):
    for i in list1:
        count=0
        for j in list1:
            if i == j:
                count+=1
        print(f"The element {i} occured {count} times")
list1=list(map(int,input("Enter the list elements").split()))
freq(list1)
