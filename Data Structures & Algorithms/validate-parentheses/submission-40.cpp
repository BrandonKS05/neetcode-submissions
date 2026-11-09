class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> d = {{')', '('}, {'}', '{'}, {']','['}};
        stack<char> seen;
        for (const auto& c: s){
            if (d.contains(c)){
                if (seen.empty() || d[c] != seen.top()){
                    return false;
                }
                seen.pop();
            }
            else  seen.push(c);
              
            
        }
        return seen.empty()? true: false;
    }
};
