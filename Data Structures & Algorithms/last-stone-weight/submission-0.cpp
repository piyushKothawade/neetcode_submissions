class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int>pq(begin(stones),end(stones));

        while(pq.size() > 1){
            int n1 = pq.top(); pq.pop();
            int n2 = pq.top(); pq.pop();

            if(n1 != n2){
                pq.push(abs(n1 - n2));
            }
        }
        if(pq.size() == 1) return pq.top();        
        return 0;        
    }
};
