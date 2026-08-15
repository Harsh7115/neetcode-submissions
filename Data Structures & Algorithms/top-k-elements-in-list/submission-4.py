class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        top = heapq.nlargest(k, count, key= lambda num: count[num])
        return top
