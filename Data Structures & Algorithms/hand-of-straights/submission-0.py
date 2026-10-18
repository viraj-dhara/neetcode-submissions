class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0 : return False        
        
        hand.sort()
        count = Counter(hand)

        for card in hand :

            start = card
            while count[start] :
                start -= 1
            while start <= card :
                if count[start] :
                    for j in range(groupSize) :
                        if not count[start+j] :
                            return False
                        count[start+j] -= 1
                start += 1

        return True
        