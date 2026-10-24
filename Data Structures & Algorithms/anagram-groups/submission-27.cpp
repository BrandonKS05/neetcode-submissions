class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> hashmap;
        std::vector<std::vector<std::string>> res;
        for(std::string s: strs){
            std::string copy = s;
            std::sort(copy.begin(), copy.end());
            hashmap[copy].push_back(s);
        }
        for(const auto& [key, val]: hashmap){
            res.push_back(val);
        }
        return res;
    }
};
