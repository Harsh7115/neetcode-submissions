class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            variable = 1
            for j in range(len(nums)):
                if i != j:
                    variable *= nums[j]
            
            new_list.append(variable)

        return new_list        