class Solution {
public:
    void f(int i, vector<int>& v, vector<vector<int>>& master, vector<int>& nums) {
        if(i == nums.size()) {
            master.push_back(v);
            return;
        }

        // taking this element
        v.push_back(nums[i]);
        f(i+1, v, master, nums);
        v.pop_back();
        // don't take the current element & any other same elements
        while(i < nums.size() && nums[i] == nums[i+1]) {
            i++;
        }
        f(i+1, v, master, nums);
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> v;
        vector<vector<int>> master;
        f(0, v, master, nums);
        return master;
    }
};
