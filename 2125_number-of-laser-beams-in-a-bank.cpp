#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int numberOfBeams(vector<string> &bank)
    {
        int count = 0;
        for (int i = 0; i < bank.size() - 1; i++)
        {
            for (int j = 0; j < bank[0].size(); j++)
            {
                cout << bank[i] << bank[j] << endl;
            }
        }
        // cout << count << endl;
        // return count;
    }
};

int main()
{
    Solution nOB;
    vector<string> arr = {"011001", "000000", "010100", "001000"};
    nOB.numberOfBeams(arr);

    return 0;
}
