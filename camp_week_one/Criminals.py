T = int(input())
for _ in range(T):

    length = int(input())
    evilness = list(map(int, input().split()))
    total = 0
    zero = 0

    for i in range(length-1):
        total += evilness[i]
        if total > 0 and evilness[i] == 0:
            zero += 1
    print(zero + total) 
