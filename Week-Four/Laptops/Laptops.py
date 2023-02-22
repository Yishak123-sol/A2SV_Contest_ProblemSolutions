N = int(input())
laptops = []

for _  in range(N):
    price, quality = list(map(int, input().split()))
    laptops.append((price, quality))

laptops.sort()
maxval = 0
for i in range(N-1):
    maxval = max(maxval, laptops[i][1])
    if maxval > laptops[i+1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
