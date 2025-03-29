class Solution:
    def reverseString(self, s):
        lenOfS = len(s)
        left = 0
        right = lenOfS - 1

        while left < right:
            first = s[left]
            end = s[right]
            temp = ""

            temp = first
            first = end
            end = temp

            s[left] = first
            s[right] = end

            left += 1
            right -= 1

        # print(s)
        return s


newReverse = Solution()
print(newReverse.reverseString(["h", "e", "l", "l", "o"]))
