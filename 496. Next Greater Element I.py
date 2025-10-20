class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        nextGreater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)

        while stack:
            nextGreater[stack.pop()] = -1

        return [nextGreater[num] for num in nums1]


newNextGreater = Solution()
print(newNextGreater.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
