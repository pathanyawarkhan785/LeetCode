class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lowerCase = upperCase = digit = specialCharPresence = False
        specialChar = "!@#$%^&*()-+"

        for i in range(len(password)):
            if i > 0 and password[i] == password[i - 1]:
                return False

            if password[i].islower():
                lowerCase = True
            elif password[i].isupper():
                upperCase = True
            elif password[i].isdigit():
                digit = True
            elif password[i] in specialChar:
                specialCharPresence = True

        return lowerCase and upperCase and digit and specialCharPresence


newStrong = Solution()
print(newStrong.strongPasswordCheckerII("IloveeLe3tcode!"))
