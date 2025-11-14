class Solution:
    def findKthLargest(self, array: list[int], k: int) -> int:
        if not array:
            return []
        min_elem = min(array)
        max_elem = max(array)
        elem_range = max_elem - min_elem + 1
        count = [0] * elem_range
        for num in array:
            count[num - min_elem] += 1
        result = []
        for i in range(elem_range):
            result.extend([i + min_elem] * count[i])
        return result[-k]