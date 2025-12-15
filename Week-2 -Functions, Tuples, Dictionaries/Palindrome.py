stri=input("Enter a string: ")
rev=stri[::-1]
if stri==rev:
    print("IS a palindrome")
else:
    print("IS NOT a palindrome")
stri=input("Enter a string: ")
#Second method
def palindrome(stri):
    rev = ""
    for i in stri:
               rev=i+rev
    if rev==stri:
            print("Is a palindrome")
    else:
            print("Not a palindrome")
palindrome(stri)
