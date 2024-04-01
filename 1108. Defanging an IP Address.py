class Solution:
    def defangIPaddr(self, address):
        for i in range(0, len(address)):
            if address[i] == ".":
                temp = address.replace(address[i], "[.]")
        return temp


newDefangIP = Solution()
print(newDefangIP.defangIPaddr("1.1.1.1"))
