class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean dup=false;
        for(int i=0;i<nums.length-1;i++)
        {
            for(int j=i+1;j<nums.length;j++)
            {
                if(num[i]==num[j])
                {
                    dup=true;
                    break;
                }
            }
        }
        return dup;
    }
}