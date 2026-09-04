class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. we need to make it so that for every unique index, that we can return an array that contains the values, and then go through that array adn return that array. 


        count = {} 
        freq=[[]for i in range(len(nums)+1)]

        for num in nums: 
            count[num] = 1 + count.get(num,0) # 0 stops type error here. 
        for num, cnt in count.items(): 
            freq[cnt].append(num) 


        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]: 
                res.append(num)
                if len(res) == k: 
                    return res
            

    


        
            




        