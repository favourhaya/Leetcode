import java.util.Dictionary;
import java.util.Hashtable;


class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer,Integer> ans = new Hashtable<>();

        for (int i = 0; i < nums.length; i++){
            int arg = target - nums[i];

            if (ans.containsKey(nums[i])){
                return new int[] {i,ans.get(nums[i])};
            }
            else{
                ans.put(arg,i);
            }
        }
           return new int[] {};
    }
}