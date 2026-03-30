class MedianFinder {
    priority_queue<int,vector<int>> pq1;
    priority_queue<int,vector<int>,greater<int>> pq2;
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        int totalSize = pq1.size() + pq2.size();
        if(totalSize % 2 == 0){
            // pq1.size() == pq2.size()
            if(!pq2.empty() && num >= pq2.top()){
                pq2.push(num);
                pq1.push(pq2.top());
                pq2.pop();
            }
            else{
                pq1.push(num);
            }
        }
        else{
            if(!pq2.empty() && num >= pq2.top()){
                pq2.push(num);
            }
            else{
                pq1.push(num);
                pq2.push(pq1.top());
                pq1.pop();
            }
        }
    }
    
    double findMedian() {
        int totalSize = pq1.size() + pq2.size();
        // cout<<pq1.size()<<endl;
        // cout<<pq2.size()<<endl;
        // if(pq2.size() == 1) cout<<pq2.top()<<endl;
        if(totalSize == 0) return 0.0;
        if(totalSize % 2 == 0) return ((pq1.top() + pq2.top()) / 2.0);
        else return pq1.top();
    }
};
