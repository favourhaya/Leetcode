class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Left = 0
        checked = set()

        for Right in range(len(nums)):
            if abs(Left - Right) > k:
                checked.remove(nums[Left])
                Left+=1
            if nums[Right] in checked:
                return True
            checked.add(nums[Right])
        return False