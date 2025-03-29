class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split(".")))
        v2_parts = list(map(int, version2.split(".")))

        max_len = max(len(v1_parts), len(v2_parts))

        for i in range(max_len):

            v1_part = v1_parts[i] if i < len(v1_parts) else 0
            v2_part = v2_parts[i] if i < len(v2_parts) else 0

            print(v1_part, v2_part)

            if v1_part < v2_part:
                return -1
            elif v1_part > v2_part:
                return 1

        return 0


newCompare = Solution()
print(newCompare.compareVersion("1.2", "1.10"))
