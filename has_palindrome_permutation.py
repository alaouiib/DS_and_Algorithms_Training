"""
Problem: Write an efficient function that checks whether
 "any" permutation  of an input string is a palindrome. 
 Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"""


def has_palindrome_permutation(the_string):
    # Check if any permutation of the input is a palindrome
    # sol 1 perso
    l = len(the_string)
    s = set(the_string)
    # if the length is odd
    if l % 2 == 0:
        if len(s) == l/2:
            return True
    # if the length is even
    elif l % 2 != 0:
        if len(s) == 1 + (l-1)/2:
            return True
    return False


def has_palindrome_permutation2(the_string):
    # sol 2 inspired from sol
    unique = set()
    for e in the_string:
        if e in unique:
            unique.remove(e)
        else:
            unique.add(e)

    return len(unique) <= 1
