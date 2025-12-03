text = input("Enter your text: ")
def count_vow(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count=0
    for char in text:
        if char in vowels:
            count=count+1

    print(count)
count_vow(text)
