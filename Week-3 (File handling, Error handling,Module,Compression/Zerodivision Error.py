a=int(input("Enter a number: "))
try:
    b=10/a
    print(b)
except Exception as e:
    print("Division by zero",e)
else:
    print("The program has ran succesfully")
finally:
    print("I will run no matter what")
