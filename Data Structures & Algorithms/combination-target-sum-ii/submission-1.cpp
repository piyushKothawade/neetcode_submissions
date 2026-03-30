class Solution {
public:
    void f(int i, vector<int>& v, vector<vector<int>>& master, vector<int>& candidates, 
    int target, int& imdSum) {
        if (imdSum > target) return;

        if(imdSum == target) {
            master.push_back(v);
            return;
        }
        
        if(i == candidates.size()) {
            if(imdSum == target) {
                master.push_back(v);
            }
            return;
        }

        // not choose a particular number, then don't choose any number equal to it
        int currNum = candidates[i];
        int j = i;
        while(j < candidates.size() && candidates[j+1] == currNum) {
            j++;
        }
        f(j+1, v, master, candidates, target, imdSum);
        v.push_back(candidates[i]);
        imdSum += candidates[i];
        f(i+1, v, master, candidates, target, imdSum);
        v.pop_back();
        imdSum -= candidates[i];

        return;
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> v;
        vector<vector<int>> master;
        int imdSum = 0;
        f(0, v, master, candidates, target, imdSum);
        return master;
    }
};
