from auto_test import *

class Solution(object):
# ------------------------Your Solution in here-----------------------------------------------
    def majority(self, nums):





# --------------------------------------------------------------------------------------------
#                   The function should return a boolean (True/False)


def solution_testings():
    _ = Solution()
    for nums, answer in majority_list:
        print(f"testing nums {nums} for majority")
        res = _.majority(nums)
        if res == answer:
            print(f"function passed!")
        else:
            raise Exception(f"Your function returned {res}, but the result should be {answer}")
    print("*"*25)
    print("You Did it!")
    print("*" * 25)

if __name__ == '__main__':
    solution_testings()

