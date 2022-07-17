data = []

print("Please tell me about yourself: ")

while True:
    line = input()
    if line:
        data.append(line)
    else:
        break
finalText = "\n".join(data)

print()
print(finalText)