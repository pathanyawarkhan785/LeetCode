from collections import deque


class Solution:
    def predictPartyVictory(self, senate):
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dStep = D.popleft()
            rStep = R.popleft()

            if rStep < dStep:
                R.append(dStep + len(senate))
            else:
                D.append(rStep + len(senate))

        return "Radiant" if R else "Dire"


newPredict = Solution()
newPredict.predictPartyVictory("RD")
