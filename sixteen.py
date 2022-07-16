list = eval(input("Enter a list of numbers: "))

print("Original list: ", list)
list_rev = list[::-1]
print("Reversed list: ", list_rev)

sum_list = []

for i in range(len(list)):
    a = list[i] + list_rev[i]
    sum_list.append(a)

print("Sum of list: ", sum_list)