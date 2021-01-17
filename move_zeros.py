def move_zeros(array):
    if array == []:
        return []

    if len(array) == 1 or 0 not in array:
        return array
    res = []
    l = len(array)
    c = 0
    for el in range(l):
        if array[el] == {} or array[el] == []:
            res.append(array[el])
        elif str(array[el]) == '0' or str(array[el]) == '0.0':
            c = c+1
        else:
            res.append(array[el])
    return res + [0]*c


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [
    1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [
    9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [
    "a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {
}, 0, 0, 9]) == ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros([0, 1, None, 2, False, 1, 0]) == [
    1, None, 2, False, 1, 0, 0])
print(move_zeros(["a", "b"]) == ["a", "b"])
print(move_zeros([0, 0]) == [0, 0])
print(move_zeros(["a"]) == ["a"])
print(move_zeros([0]) == [0])
print(move_zeros([False]) == [False])
print(move_zeros([]) == [])
