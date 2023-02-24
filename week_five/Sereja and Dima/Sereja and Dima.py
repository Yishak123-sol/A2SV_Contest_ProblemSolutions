length = int(input())
array = list(map(int, input().split()))
left = 0
right = length-1
seraj = dima = count1 = count2 = 0


while left <= right:
    
    if count1 == count2:
        if array[right] > array[left]:
            seraj += array[right]
            right -= 1
            
        else:
            seraj += array[left]
            left += 1
            
        count1 += 1
         
    elif count1 > count2:
        if array[right] > array[left]:
            dima += array[right]
            right -= 1
            count2 += 1
        else:
            dima += array[left]
            left += 1
            count2 += 1
        
    
        
print(seraj, dima)
