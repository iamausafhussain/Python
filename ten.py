t = eval(input("Enter a tuple: "))
number = input("Enter the element: ")
index = int(input("Enter the index position to insert: "))

t = list(t)
t.insert(index, number)
t = tuple(t)

print(t)