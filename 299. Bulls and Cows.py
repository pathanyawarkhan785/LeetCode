class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = [0] * 10
        guess_count = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[int(secret[i])] += 1
                guess_count[int(guess[i])] += 1

        for i in range(10):
            cows += min(secret_count[i], guess_count[i])

        return f"{bulls}A{cows}B"


newGetHint = Solution()
print(newGetHint.getHint("1122", "0001"))
