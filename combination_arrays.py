def solve(a):
    res = [len(set(array)) for array in a]
    n_comb = 1
    for n in res:
        n_comb = n_comb * n
    return n_comb


# print(solve([[1, 2], [4, 4], [5, 6, 6]]))
print(solve([[1, 2], [4], [5, 6]]) == 4)
print(solve([[1, 2], [4, 4], [5, 6, 6]]) == 4)
print(solve([[1, 2], [3, 4], [5, 6]]) == 8)
print(solve([[1, 2, 3], [3, 4, 6, 6, 7], [8, 9, 10, 12, 5, 6]]) == 72)
