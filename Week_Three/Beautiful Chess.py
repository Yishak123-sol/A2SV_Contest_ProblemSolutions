def beautifulChess():
    
    matrix = []
    for _ in range(8):
        arr = list(input().strip())
        matrix.append(arr)
    for i in range(6):
        if matrix[i].count("#") == 2 and matrix[i + 1].count("#") == 1 and matrix[i + 2].count("#"):
            row = i + 1
            col = matrix[i + 1].index("#")
            return str(row + 1) + " " + str(col + 1)
            
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        input()
        print(beautifulChess())
