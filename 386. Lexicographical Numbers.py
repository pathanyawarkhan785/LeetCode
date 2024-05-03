class Solution:
    def lexicalOrder(self, n):
        lst = [str(i) for i in range(1, n + 1)]
        print(lst)
        print(lst[0], type(lst[0]))
        # print(str(i))


# [1,10,11,12,13,2,3,4,5,6,7,8,9]


newLexicalOrder = Solution()
newLexicalOrder.lexicalOrder(13)
