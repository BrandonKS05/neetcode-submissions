class Solution {
public:
    bool isDecomposable(string s) {
        long long n = 1;
        long long m = 0;
        for (long long i = 1; i < s.size(); i++){
            if (s[i] == s[i - 1]){
                n++;
            }
            else{
                if (n % 3 == 1) return false;
                if (n % 3 == 2) {
                    m++;}
                n = 1;
                
            }
        
        }
        if (n % 3 == 1) return false;
        if (n % 3 == 2) m++;
           
        bool res = (m == 1)? true: false;
        return res;

    }
};
