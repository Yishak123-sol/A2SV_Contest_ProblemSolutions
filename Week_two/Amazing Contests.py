
def amazing_contest():

    length_of_list = int(input())
    Amazing_list = list(map(int, input().split(None, length_of_list)))


    amazing = Amazing_list[0]
    worest = Amazing_list[0]
    count = 0

    for i in range(1, length_of_list):

        if Amazing_list[i] > amazing:
            count += 1
            amazing = Amazing_list[i]

        elif Amazing_list[i] < worest:
            count += 1
            worest = Amazing_list[i]

    return count

print(amazing_contest())
