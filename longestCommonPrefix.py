from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # take the string with the least number of caracters
    # ->"flow"
    # -> generate prefixes: dict = {"flow":0,"flo":"","fl":0,"f":0}
    # iterate over dict, take the first one with value = len(srts)
    if not strs:
        return ""
    min_length, index_of_smallest = 99999, -1
    d = dict()
    temp_string = ""
    for i, s in enumerate(strs):
        if len(s) < min_length:
            index_of_smallest = i
            min_length = len(s)

    #  print(strs[index_of_smallest]) -> # flow
    smallest_string = strs[index_of_smallest]
    if smallest_string == "":
        return ""
    # initialise our dictionnary with potential prefixes
    for prefix in smallest_string:
        temp_string = temp_string + prefix
        d[temp_string] = 0
    # print(d)  # -> {'f': 0, 'fl': 0, 'flo': 0, 'flow': 0}

    for prefix in d:
        for s in strs:
            if prefix in s and s.index(prefix) == 0:
                d[str(prefix)] += 1

    if d.values() and max(d.values()) < len(strs):
        return ""
    results = [k for k in d if d[k] == max(d.values())]
    print(d)
    return max(results)


print("LCP:", longestCommonPrefix(["flower", "flow", "flight", "flwow"]))
print("LCP:", longestCommonPrefix(["dog", "racecar", "car"]))
print("LCP:", longestCommonPrefix(["abab", "aba", ""]))
