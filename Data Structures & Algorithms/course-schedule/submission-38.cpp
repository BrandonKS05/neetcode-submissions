class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<long long, std::vector<long long>> graph;
        std::vector<long long> in_degree(numCourses);
        for (long long i = 0; i < numCourses; i++){
            graph[i] = std::vector<long long>();
        }
        for(std::vector<int> edge: prerequisites){
            long long v = static_cast<long long>(edge[0]);
            long long u = static_cast<long long> (edge[1]);
            graph[u].push_back(v);
            in_degree[v] = in_degree[v] + 1;
        }
        std::deque<long long> dq;
        for (long long i = 0; i < in_degree.size(); i++){
            if (in_degree[i] == 0){;
                dq.push_back(i);
            }
        }
        long long completed = 0;

        while (dq.size() != 0){
            long long u = dq.front();
            completed++;
            dq.pop_front();
            
            for (long long v: graph[u]){
                in_degree[v] = in_degree[v] - 1;
                
                if (in_degree[v] == 0){
                    dq.push_back(v);
                }
            }
        }
        return numCourses == completed;
    }
};
