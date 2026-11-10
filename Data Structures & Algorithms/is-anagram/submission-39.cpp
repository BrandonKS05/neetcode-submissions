class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<long long> marc(26); 
        for(auto c: s){
            long long idx = c - 'a';
            marc[idx] += 1;
        }
        for(auto c: t){
            long long idx = c - 'a';
            marc[idx] -= 1;
        }
        for(long long num: marc){
            if (num !=0) return false;
        }
        return true;
    }
};
