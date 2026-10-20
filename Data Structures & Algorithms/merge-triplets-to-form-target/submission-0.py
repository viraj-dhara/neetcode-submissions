class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        
        triplets_new = list()
        for triplet in triplets[:] :
            if not(triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]) : 
                triplets_new.append(triplet)

        print(triplets_new)

        for triplet in triplets_new :
            for i in range(3) :
                if triplet[i] == target[i] :
                    target[i] = 0
            if target == [0,0,0] : return True

        return False
            