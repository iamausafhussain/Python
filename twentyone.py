string = input("Enter a string: ")
list = []
for ch in string:
    list.append(ch)

tuple = tuple(list)
print(tuple)