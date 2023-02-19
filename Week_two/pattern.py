
def matching():

    patterns_size = int(input())
    patterns = []
    intersect = []

    for _ in range(patterns_size):

        pattern_reader = input()
        patterns.append(pattern_reader)

    for index in range(len(pattern_reader)):
        
        temporary_set = set()
        
        for pattern_index in range(patterns_size):
            if patterns[pattern_index][index] not in temporary_set:
                temporary_set.add(patterns[pattern_index][index]) 
        
            
        if len(temporary_set) > 2:
            intersect.append("?")

        elif len(temporary_set) == 2 and "?" in temporary_set:
            difference = list(temporary_set.difference({"?"}))
            intersect.append(difference[0])
        
        elif len(temporary_set) == 2:
            intersect.append("?")

        else:
            if "?" in temporary_set:
                intersect.append("a")
                
            else:
                intersect.append(patterns[pattern_index][index])
    

    matche_string = "".join(intersect)

    
    return matche_string

print(matching())
        
