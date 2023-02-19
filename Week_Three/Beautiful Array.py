import sys

input = sys.stdin.readline

length = int(input())
arr = list(map(int, input().split()))

one = []
two = []
three = []

for i in range(length):
  
  if arr[i] < 0:
    one.append(arr[i])
    
    
  elif arr[i] == 0:
    three.append(0)
    
  else:
    two.append(arr[i])

if len(one) % 2 == 0:
  three.append(one.pop())
  
if len(one) > 2 :
  two.append(one.pop())
  two.append(one.pop())

print(len(one), *one)
print(len(two), *two)
print(len(three), *three)
    
