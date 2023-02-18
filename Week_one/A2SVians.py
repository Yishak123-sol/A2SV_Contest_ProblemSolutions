length = int(input())
name_list = list(map(str, input().split()))
flagged_name = set((map(str, input().split())))
count = 0

for i in range(len(name_list)):
    word = name_list[i]
    map = {}
    for j in range(len(word)):
        if word[j] in map:
            map[word[j]] += 1
        else:
            map[word[j]] = 1

    check = set()
    for key, value in map.items():
        check.add(value)
        
    if word not in flagged_name and len(check) == 1:
        count += 1
        
print(count)
