class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.arr = [0,0]

        for i in range(0,len(nums),1):
            for j in range(i+1, len(nums),1):
                if (nums[i]+nums[j] == target):
                    self.arr[0] = i
                    self.arr[1] = j
                

        return self.arr
