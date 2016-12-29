# -*- coding: utf-8 -*-

def findDisappearedNumbers(nums):
    ''' my version'''
    return list({i for i in xrange(1, len(nums)+1)} - set(nums))
    ''' disscusion: use index and negative numbers to find which lost 
    for i in range(len(nums)):
		index = abs(nums[i]) - 1
		nums[index] = - abs(nums[index])
	    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    '''
    

print findDisappearedNumbers([4,3,2,7,8,2,3,1])

    
