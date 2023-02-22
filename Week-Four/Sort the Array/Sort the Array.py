def can_sort_by_reversing(n, arr):

    start = None
    end = None

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            start = i
            break

    if start is None:
        return ("yes", 1, 1)

    for i in range(n-1, start, -1):
        if arr[i] < arr[i-1]:
            end = i
            break

    if sorted(arr[start:end+1]) == arr[start:end+1][::-1]:
        if (start > 0 and arr[end] < arr[start-1]) or (end < n-1 and arr[start] > arr[end+1]):
            return ("no", 0, 0)

        return ("yes", start+1, end+1)

    return ("no", 0, 0)


N = int(input())
arr = list(map(int, input().split()))

result = can_sort_by_reversing(N,arr)

print(result[0])

if result[0] == "yes":
    print(result[1], result[2])
