listInput = eval(input("Enter a list of numbers to remove duplicates: "))

list_rem = list(dict.fromkeys(listInput))

print(list_rem)