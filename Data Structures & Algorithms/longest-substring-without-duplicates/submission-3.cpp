class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length() == 0) return 0;
        map<char,int> mp;
        int maxi = 1;
        int startIdx = 0, j = 0;
        while(j < s.length()){
            char ch = s[j];
            if(mp.find(ch) != mp.end()){
                int idx = mp[ch];
                if(idx >= startIdx){
                    maxi = max(maxi, j - startIdx);
                    startIdx = idx + 1;
                }
            }
            mp[ch] = j;
            j++;
        }
        maxi = max(maxi, j - startIdx);
        return maxi;
    }
};
