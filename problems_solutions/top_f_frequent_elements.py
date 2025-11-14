class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        res = [item[0] for item in sorted_counts[:k]]

        return res

