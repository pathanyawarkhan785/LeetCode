#include <iostream>
#include <vector>
#include <limits>

using namespace std;

class Solution
{
public:
    int maximumDifference(vector<int> &nums)
    {
        int minVal = numeric_limits<int>::max();
        int maxDiff = -1;

        for (int num : nums)
        {
            if (num > minVal)
                maxDiff = max(maxDiff, num - minVal);
            minVal = min(minVal, num);
        }

        return maxDiff;
    }
};

int main()
{
    Solution newMax;
    vector<int> nums = {7, 1, 5, 4};
    int result = newMax.maximumDifference(nums);

    cout << "max diff: " << result << endl;

    return 0;
}
