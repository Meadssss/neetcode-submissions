import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ", "").translate(str.maketrans("", "", string.punctuation)).lower() 

        c = 0
        t = len(st) - 1 - c

        while c < t:
            if st[c] != st[t]:
                return False
            else:
                c += 1
                t -= 1
        return True 
