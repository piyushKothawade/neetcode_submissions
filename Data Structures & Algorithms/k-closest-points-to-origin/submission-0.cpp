#include <cmath>
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<double, int>> pq;
        int n = points.size();
        vector<vector<int>> res;
        for(int i = 0; i < k; i++){
            pq.push({sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1]), i});
        }

        for(int i = k; i < n; i++){
            int dist = sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1]);
            if(dist < pq.top().first){
                pq.pop();
                pq.push({dist, i});
            }
        }

        while(!pq.empty()){
            res.push_back(points[pq.top().second]);
            pq.pop();
        }
        return res;
    }
};
