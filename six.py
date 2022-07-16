l = eval(input("Enter a list: "))

l1 = sorted(l)

if len(l) > 2:
    print("Second Largest : ", l1[-2])
    print("Second Smallest: ", l1[1])
elif len(l) == 2:
    print("Second Largest: ", l1[0])
    print("Second Smallest: ", l1[0])
elif len(l) == 1:
    print("Second Largest: ", l1[0])
    print("Second Smallest: ", l1[0])