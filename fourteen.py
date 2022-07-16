# [(10,20,40),(40,50,60),(70,80,90)]

list__tuple = eval(input("Enter list of tuples: "))
print("Original list of tuples: ", list__tuple)
res = [list(elem) for elem in list__tuple]

for ch in res:
    for i in range(len(ch)):
        if i == 2:
            ch[i] = 100

opp = [tuple(elem) for elem in res]
print("Output: ", opp)