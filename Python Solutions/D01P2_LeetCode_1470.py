class Solution(object):
    def shuffle(self, nums:list[n], n:int)->list[n]:
        for i in range(n-1):
            nums.insert(n+i,nums.pop(1))
        return nums
