t = eval(input("Enter a tuple: "))
number = int(input("Enter the element: "))
index = int(input("Enter the index position to insert: "))

l = list(t)

l.insert(index, number)

t = tuple(l)
print(t)

