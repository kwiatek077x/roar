n = int(input("Text: "))
sumOfPaired = 0
i = 0
j = 0

while i < n:
    j += 1
    if j % 2 == 0:
        sumOfPaired += j
        i += 1

print(sumOfPaired)