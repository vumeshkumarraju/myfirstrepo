def CombinationRepetitionUtil(chosen, arr, index, r, start, end):
    if index == r:
        print(chosen)
        return
    if start > n:
        return
    chosen[index] = arr[start]
    CombinationRepetitionUtil(chosen, arr, index + 1, r, start, end)
    CombinationRepetitionUtil(chosen, arr, index, r, start + 1, end)


def CombinationRepetition(arr, n, r):
    chosen = [0] * r
    CombinationRepetitionUtil(chosen, arr, 0, r, 0, n)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
r = 3
n = len(arr) - 1
ls1 = []
CombinationRepetition(arr, n, r)
