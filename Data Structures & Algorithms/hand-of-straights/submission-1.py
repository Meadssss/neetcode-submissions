class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        for num in sorted(count):
            c = count[num]
            if c == 0:
                continue
            for i in range(num, num + groupSize):
                if count[i] < c:
                    return False
                count[i] -= c
        return True