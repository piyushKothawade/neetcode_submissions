class Twitter {
    int count;
    unordered_map<int,vector<vector<int>>> tweetMap;
    unordered_map<int,set<int>> followeeMap;
public:
    Twitter() {
        count = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        cout<<userId<<" "<<tweetId<<endl;
        tweetMap[userId].push_back({tweetId, count});
        count++;
    }
    
    vector<int> getNewsFeed(int userId) {

        priority_queue<vector<int>, vector<vector<int>>> pq;
        int rem = 10;
        vector<int> res;
        // iterate through all the people whom the userId follows
        // cout<<userId<<endl;
        for(auto it: followeeMap[userId]){
            // cout<<it<<endl;
            int n = tweetMap[it].size();
            if(n > 0) {
                vector<int> tweetDetails = tweetMap[it][n-1];
                pq.push({tweetDetails[1], tweetDetails[0], it, n-1});
                // cout<<tweetDetails[0]<<endl;
            }
        }
        // also, push his own tweets
        int n = tweetMap[userId].size();
        if(n > 0) pq.push({tweetMap[userId][n-1][1], tweetMap[userId][n-1][0], userId, n-1});

        while(rem > 0 && !pq.empty()){
            rem--;
            vector<int> best = pq.top();
            int index = best[3];
            int userId = best[2];
            cout<<"index: "<<index<<endl;
            pq.pop();
            res.push_back(best[1]);
            if(index - 1 >= 0) pq.push({tweetMap[userId][index - 1][1], tweetMap[userId][index - 1][0], 
            userId, index - 1});
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        if(followeeId == followerId) return;
        followeeMap[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        followeeMap[followerId].erase(followeeId);
    }
};
