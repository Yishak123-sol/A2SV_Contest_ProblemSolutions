
test_case = int(input())

for _ in range(test_case):
    length, k = map(int, input().split())
    array = list(map(int, input().split()))
    left = 0
    res = 0
    
    for right in range(1,len(array)):
        if array[right]*2 <= array[right-1]:
            left = right
            
        if right-left >= k:
            res += 1
            left += 1
            
    print(res)
