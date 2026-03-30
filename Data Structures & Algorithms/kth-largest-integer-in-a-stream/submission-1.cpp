class KthLargest {
public:
    vector<int> stream;
    int kval;
    priority_queue<int, vector<int>, greater<int>> pq;

    KthLargest(int k, vector<int>& nums) {
        stream = nums;
        kval = k;

        for(int i = 0; i < min(k, int(stream.size())); i++){
            pq.push(stream[i]);
        }

        if(stream.size() - k > 0){
            for(int i = k; i < stream.size(); i++){
                int top = pq.top();
                if(stream[i] > pq.top()){
                    pq.pop();
                    pq.push(stream[i]);
                }
            }
        }
    }
    
    int add(int val) {
        // Heap size is surely <= k
        if(pq.size() < kval) pq.push(val);

        else{
            if(val > pq.top()){
                pq.pop();
                pq.push(val);
            }
        }
        return pq.top();
    }
};
