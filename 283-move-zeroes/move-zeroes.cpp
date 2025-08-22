class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int indexpos=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if (nums[i]!=0){
                nums[indexpos++]=nums[i];
            }
        }
        for(int i=indexpos;i<n;i++){
            nums[i]=0;
        }
        
    }
};