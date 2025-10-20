#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int superPow(int a, vector<int> &b)
    {
        // cout << a << endl;

        for (int i = 0; i < b.size(); i++)
        {
            cout << b[i] * i << endl;
        }
    }
};

int main()
{
    int a = 2;
    vector<int> b = {3, 7};

    int res = Solution().superPow(a, b);
    return 0;
}
