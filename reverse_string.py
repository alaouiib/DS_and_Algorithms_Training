# In place
# O(n) Time, O(1) Space
def reverseString(s):
    """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        left_pointer += 1
        right_pointer -= 1

# Not in place
# O(n) Time, O(N^2) Space at worst (n+n-1+n-2+..+1 ~ n^2)


def reverseString_rec(s):
    """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
    if len(s) == 0:
        return s
    return reverseString_rec(s[1:]) + list(s[0])


def reverseString_pythonic(s):
    s.reverse()
    return s


if __name__ == "__main__":
    string_test = ["H", "a", "m", "e", "t"]
    print("String_test:", string_test)
    print("Recursive: ", reverseString_rec(string_test))

    reverseString(string_test)
    print("Iterative: ", string_test)

    string_test = ["H", "a", "m", "e", "t"]
    print('Pythonic way', reverseString_pythonic(string_test))
