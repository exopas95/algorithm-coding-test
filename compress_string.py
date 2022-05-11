s = list(input())

count = 0
length = len(s)
for i in range(0, length):
    num = i + 1
    for j in range(0, length, num):
        if s[j*num:(j+1)*num] == s[(j+1)*num:(j+2)*num]:

