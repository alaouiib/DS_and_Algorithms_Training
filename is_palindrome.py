
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
        """
    # A space is palindrome
    if s == ' ':
        return True
    l_left, l_right = 0, len(s)-1
    while l_left <= l_right:
        # The second condition is for puntuations
        while not s[l_left].isalnum() and l_left < len(s) - 1:
            l_left += 1
        while not s[l_right].isalnum() and l_right >= 0:
            l_right -= 1
        if(s[l_left].lower() != s[l_right].lower()):
            return False
        else:
            l_left += 1
            l_right -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama") == True)
print(isPalindrome("race a car") == False)
print(isPalindrome("a.") == True)
