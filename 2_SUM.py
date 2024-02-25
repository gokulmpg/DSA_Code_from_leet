class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        foundSolution = False

        i =0

        solutionList = []
        while i < len(nums) and not foundSolution:    
            j = i + 1
            while j < len(nums) and not  foundSolution:
                if nums[i] + nums[j] == target:
                    foundSolution = True
                    solutionList.append(i)
                    solutionList.append(j)
                j += 1
            i +=1
        return solutionList
