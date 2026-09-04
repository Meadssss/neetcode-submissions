class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Same Characters, Same occurence

        def check_freq(x): 
            return {c: x.count(c) for c in set(x)}

        return check_freq(s) == check_freq(t)