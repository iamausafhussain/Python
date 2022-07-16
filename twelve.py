tuple = eval(input("Enter a tuple: "))

list = list(tuple)
print(list)

res__list = []

for ch in list:
    if list.count(ch) > 1:
        if ch in res__list:
            continue
        else:
            res__list.append(ch)
        continue

print("Repeted Items in tuple are: ")
for ch in res__list:
    print(ch, end=" ")
