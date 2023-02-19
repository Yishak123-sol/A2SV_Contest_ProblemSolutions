
testcase = int(input())

for j in range(testcase):
    
    t = input()
    text = t.split()
    dic = {}
    
    for char in text:
        
        word = []
        number = []
        
        for num in char:
            if num.isnumeric():
                number.append(num)
            else:
                word.append(num)
            
        word = "".join(word)
        number = "".join(number)
        dic[word] = int(number)

    dic = sorted(dic.items(), key=lambda s: s[1])
    
    text = ""
    for i in range(len(dic)):
        if i < len(dic)-1:
            text += dic[i][0] + " "
            
        else:
            text += dic[i][0]
        
    print(text)
    
    
    
    
    
    
    
    
