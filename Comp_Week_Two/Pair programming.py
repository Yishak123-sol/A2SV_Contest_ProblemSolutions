n, k = list(map(int, input().split()))
solved_time = list(map(int, input().split()))

solved_time.sort()
left = 0
right = len(solved_time)-1
ans = 0
while k > 0:
    mid = left + (right-left)//2
    deduct =  min((mid+1)-left, k)
    ans += solved_time[mid] * deduct
    k -= deduct
    left = mid +  1

print(ans)
