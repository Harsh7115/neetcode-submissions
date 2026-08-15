class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k_largest = heapq.nlargest(k, nums)

        top = k_largest[-1]

        return top
        