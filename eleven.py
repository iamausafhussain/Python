user__tuple = eval(input("Enter a tuple of elements: "))
rem = (int(input("Enter the position to remove: ")))-1

print("Original Tuple: ", user__tuple)
user__tuple = user__tuple[:rem] + user__tuple[rem+1:]

print("After removal: ", user__tuple)
