# Brute Force solution

# I'm going to use List in this file, so go fetch it from the typing module before running anything else.
from typing import List

class Solutoin:
    #  arrow defines whta type of value the function is expected to return
    def Twosum (self,nums:list[int],target:int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return[]