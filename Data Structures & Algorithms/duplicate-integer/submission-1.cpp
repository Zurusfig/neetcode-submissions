class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> set_nums;
        for(int n : nums){
            auto it = set_nums.find(n);
            if(it != set_nums.end()){
                return true;
            }
            set_nums.insert(n);
        }
        return false;
    }
};