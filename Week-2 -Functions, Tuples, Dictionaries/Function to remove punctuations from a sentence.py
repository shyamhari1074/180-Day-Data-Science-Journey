import string
str=input("Enter a string: ")
def remove_punctuation(str):
       clean_text=" "
       for ch in str:
          if ch not in string.punctuation:
             clean_text=clean_text+ch
       print(clean_text)
remove_punctuation(str)
