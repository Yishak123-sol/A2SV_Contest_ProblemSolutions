length = int(input())
pronounce = []

for i in range(length):
    pronounce.append(input())

for j in range(length):
    print(pronounce[j][0:2]+"...", pronounce[j]+"?")
