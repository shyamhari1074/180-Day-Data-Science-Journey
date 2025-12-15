vowels=['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
str=input("Enter a string: ")
count=0
for char in str:
    if char in vowels:
        count+=1
print(count)
