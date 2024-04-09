from auto_test import *

class Solution(object):
# ------------------------Your Solution in here-----------------------------------------------
    def twosum(self, nums, target):




# --------------------------------------------------------------------------------------------
#                   The function should return a list with two numbers [x,y]


def solution_testings():
    _ = Solution()
    for nums, target in two_sum_list:
        print(f"testing nums {nums} for target {target}")
        res = _.twosum(nums, target)
        if nums[res[0]] + nums[res[1]] == target:
            print(f"function passed!")
        else:
            raise Exception(f"Your function returned {res}, which results in {nums[res[0]]} + {nums[res[1]]} =/= {target}")
    print("*"*25)
    print("You Did it!")
    print("*" * 25)

if __name__ == '__main__':
    solution_testings()

