l = eval(input("Enter a list: "))
number = int(input("Enter the number: "))

for i in l:
    if i > number:
        print(i, end=" ")