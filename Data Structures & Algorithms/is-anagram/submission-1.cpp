class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        map<char,int> mp1;
        map<char,int> mp2;
        for(int i = 0; i < s.size(); i++){
            if(mp1.find(s[i]) == mp1.end()){
                mp1[s[i]] = 0;
            }
            if(mp2.find(t[i]) == mp2.end()){
                mp2[t[i]] = 0;
            }
            mp1[s[i]]++;
            mp2[t[i]]++;
        } 
        return mp1 == mp2;
    }
};
