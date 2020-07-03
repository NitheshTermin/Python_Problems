class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind1 = -1
        ind2 = 0
        found = False
        for num in nums:
            ind2 = ind1 + 1
            ind1 += 1
            for addnum in nums[ind1 + 1:]:
                ind2 += 1
                if num + addnum == target:
                    found = True
                    # ind1 = nums.index(num)
                    # ind2 = nums.index(addnum)
                    break
            if found:
                break        
        return [ind1, ind2]
        
