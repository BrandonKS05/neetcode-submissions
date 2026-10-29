class Solution {
public:
    unordered_map<int, int> seen;
    int dfs(int n){
        if (seen.contains(n)){
            return seen[n];
        }
        else if (n == 1) return 1;
        else if (n == 2) return 2;
        else {
            seen[n] = climbStairs(n - 1) + climbStairs(n - 2);
            return seen[n];

        }
        }
 
    int climbStairs(int n) {
      
        return dfs(n);
        
    }
   
};
