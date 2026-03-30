class Solution {
public:
    void f(int i, vector<int>& v, vector<vector<int>>& master, vector<int>& nums) {
        if (i == nums.size()) {
            master.push_back(v);
            return;
        }

        for(int j = i; j < nums.size(); j++) {
            swap(nums[j], nums[i]);
            v.push_back(nums[i]);
            f(i + 1, v, master, nums);
            v.pop_back();
            swap(nums[j], nums[i]);
        }
        return;
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> v;
        vector<vector<int>> master;
        f(0, v, master, nums);
        return master;
    }
};
