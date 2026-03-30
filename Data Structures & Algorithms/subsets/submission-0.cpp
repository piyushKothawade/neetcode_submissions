class Solution {
public:
    void f(int i, vector<int>& v, vector<vector<int>>& master, vector<int>& nums) {
        if(i == nums.size() - 1) {
            master.push_back(v);

            v.push_back(nums[i]);
            master.push_back(v);

            v.pop_back();
            return;
        }

        f(i+1, v, master, nums);
        v.push_back(nums[i]);
        f(i+1, v, master, nums);
        v.pop_back();
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> v;
        vector<vector<int>> master;
        f(0, v, master, nums);
        return master;
    }
};