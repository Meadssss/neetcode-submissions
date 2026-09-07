class Solution:
    def isValid(self, s: str) -> bool:
        #takes around 7 mins 
        Q = [] 
        matching = { ")": "(", "}": "{", "]": "["}
        for i in s:
            if i in matching: 
                if Q and Q[-1] == matching[i]:
                    Q.pop()
                else:
                    return False

            else:
                Q.append(i) 


        return len(Q) == 0 