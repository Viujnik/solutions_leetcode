class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        array = nums
        if not array:
            return []
        max_elem = max(array)
        count_arr = [0] * (max_elem + 1)
        for num in array:
            count_arr[num] += 1

        for i in range(1, max_elem + 1):
            count_arr[i] += count_arr[i - 1]

        for num in array[::-1]:
            nums[count_arr[num] - 1] = num
            count_arr[num] -= 1
