class Solution:
    def nextGreaterElement(self, nums1, nums2):
        mapping = {}          # value -> its next greater element
        stack = []            # values from nums2 still waiting

        for num in nums2:
            while stack and num > stack[-1]:   # num is the next-greater for everyone it beats
                mapping[stack.pop()] = num
            stack.append(num)
        # anything still on the stack never found a greater -> defaults to -1 below

        return [mapping.get(x, -1) for x in nums1]
        