test_case = int(input())

for _ in range(test_case):
  nums = list(map(int, input().split(None, 3)))
  max_val = max(nums)
  min_val = min(nums)
  
  for i in range(3):
    if nums[i] != min_val and nums[i] != max_val:
      print(nums[i])
