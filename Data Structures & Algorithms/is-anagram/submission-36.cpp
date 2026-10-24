class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        std::vector<int> counter(26);
        int l = 0;
        for(int i =0; i<s.size(); i++){
            int idx = (int)s[i] - (int)'a';
            counter[idx] += 1;
            idx = (int)t[i] - (int)'a';
            counter[idx] -= 1;
        }
        return all_of(counter.begin(), counter.end(), [](int c){return c == 0;});
    }
};
