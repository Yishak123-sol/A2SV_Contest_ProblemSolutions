T = int(input())

for _ in range(T):
    
    length, c = input().split()
    length = int(length)
    color = input()
    left = right = maxval = 0
    circle = int(length * 2)

    while right < circle:
        while right < circle and color[right%length] != c:
            right += 1
        left = right

        while right < circle and color[right%length] != 'g':
            right += 1
            
        maxval = max(maxval, right-left)
        right += 1

    print(maxval)
