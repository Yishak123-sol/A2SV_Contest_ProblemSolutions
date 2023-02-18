N = int(input())
 
for i in range(N):
 
    text = input().split()
    text = "".join(text)
    text = text.replace("#", " ")
 
    print(text)
