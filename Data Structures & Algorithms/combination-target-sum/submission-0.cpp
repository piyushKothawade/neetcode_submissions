class Solution {
public:
    void f(int i, vector<int>& v, vector<vector<int>>& master, vector<int>& nums, 
    int target, int& imdSum){
        if(imdSum > target) return;
        if(i == nums.size()){
            if(imdSum == target) {
                master.push_back(v);
            }
            return;
        }

        f(i+1, v, master, nums, target, imdSum);
        v.push_back(nums[i]);
        imdSum += nums[i];
        f(i, v, master, nums, target, imdSum);
        v.pop_back();
        imdSum -= nums[i];

        return;
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> v;
        vector<vector<int>> master;
        int imdSum = 0;
        f(0, v, master, nums, target, imdSum);
        return master;
    }
};
