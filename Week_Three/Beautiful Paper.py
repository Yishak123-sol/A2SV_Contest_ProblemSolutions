Test_case = int(input())

for i in range(Test_case):

  row1 = list(map(int, input().split(None, 2)))
  row2 = list(map(int, input().split(None, 2)))

  max_num1 = max(row1)
  max_num2 = max(row2)
  
  min_num1 = min(row1)
  min_num2 = min(row2)
  
  if max_num1 == max_num2 and (min_num2 + min_num1) == max_num1:
      print("Yes")
      
  else:
      print("No")
