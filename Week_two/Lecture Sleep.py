
def max_number_of_theorems():
    
    duration_awake = list(map(int, input().split()))
    theroems = list(map(int, input().split()))
    behavior = list(map(int, input().split()))

    total_writeDown = 0

    for index in range(duration_awake[0]):
        if behavior[index] == 1:
            total_writeDown += theroems[index]
    
    
    awake = duration_awake[1]

    total = 0
    left = 0
    max_awake_value = 0

    for index in range(duration_awake[0]):

        if index >= awake:
            
            if behavior[left] == 0:
                total -= theroems[left]
                left += 1

            else:
                left += 1
                
        if behavior[index] == 0:
            
            total += theroems[index]

        if (index-left + 1) == awake:

            max_awake_value = max(total, max_awake_value)


    return (total_writeDown + max_awake_value)
    
    

print(max_number_of_theorems())
    
