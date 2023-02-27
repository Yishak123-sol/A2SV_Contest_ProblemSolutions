length = int(input())
array = list(map(int,input().split()))
left_sum = 0
right_sum = 0
 
left = 0
a = b = 0
right = length-1
 
while left <= right:
    if right_sum >= left_sum:
        left_sum += array[left]
        left += 1
        a += 1
        
    else:
        right_sum += array[right]
        right -= 1
        b += 1
 
print(a, b)
