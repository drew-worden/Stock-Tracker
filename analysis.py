collectedData = []
file = open("data.txt", "r")
for line in file:
    line = str(line)
    cleanedString = ""
    for char in line:
        if char in "1234567890.":
            cleanedString = cleanedString + char
    collectedData.append(float(cleanedString))

print(collectedData)
