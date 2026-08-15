class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        top = heapq.nlargest(k, count, key = lambda nums: count[nums])
        return top