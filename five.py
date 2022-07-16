l1 = eval(input("Enter a list: "))
l2 = eval(input("Enter another list: "))

s1 = set(l1)
s2 = set(l2)

print(s1.intersection(s2))