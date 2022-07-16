print("Enter list of Email addresses: ")
eList = eval(input())
count = 0
names = []
cNames = []

for emails in eList:
    count += 1
    atTheRate = emails.index('@')
    names.append(emails[:atTheRate])
    cNames.append(emails[atTheRate + 1: -4])

print("Names: ", names)
print("Company: ", cNames)
    
        