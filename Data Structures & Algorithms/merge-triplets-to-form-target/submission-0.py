class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        flag = True
        mark = [0, 0, 0]

        for triplet in triplets:
            if any([triplet[j] > target[j] for j in range(3)]):
                continue

            if all([triplet[j] < target[j] for j in range(3)]):
                continue

            for j in range(3):
                if triplet[j] == target[j]:
                    mark[j] = 1

        if all(mark):
            return True
        return False

