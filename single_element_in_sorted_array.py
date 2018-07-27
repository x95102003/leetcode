def singleNonDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_size = len(nums)
        for i in xrange(0, num_size-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i] if nums[i+1] == nums[i+2] else nums[i+1]
        return nums[num_size-1]
if __name__ == '__main__':
    print(singleNonDuplicate([1,2,2,3,3]))
