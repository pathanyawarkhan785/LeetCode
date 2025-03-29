class Solution:
    def compress(self, chars):
        count = 1
        s = ""
        for i in range(len(chars) - 1):
            # print(i)

            if chars[i] == chars[i + 1]:
                count += 1

            else:

                s = s + chars[i]

                if count > 1:
                    # chars.append(str(count))
                    s = s + str(count)

                # chars.append(chars[i])
                count = 1

        # chars.append(str(count))
        s = s + chars[-1]
        if count > 1:
            s = s + str(count)

        # print(s)

        for i in range(len(s)):
            chars[i] = s[i]
        chars = chars[: len(s)]
        # print(chars)

        return len(chars)


newCompress = Solution()
print(newCompress.compress(["a", "a", "b", "b", "c", "c", "c"]))
