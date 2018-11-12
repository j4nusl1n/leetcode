#!/usr/bin/python3
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """        
    import re
    # ripped off non-word character and upper case s(case insensitive)
    s = re.sub(r"[^\w]*", "", s)
    s = s.upper()
    
    # empty string considered as valid by specification
    # also, single character is a valid case
    if s == '' or len(s) == 1:
        return True

    # compare string from both ends
    leftSide, rightSide = 0, len(s)-1
    flg = True
    while True:
        flg = s[leftSide] == s[rightSide]

        # comparison failed
        if not flg:
            break

        # move both end's pointer
        leftSide += 1
        rightSide -= 1
        
        # if both pointers meet at the middle of the string
        if leftSide > rightSide:
            break

    return flg
