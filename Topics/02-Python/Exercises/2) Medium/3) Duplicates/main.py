from auto_test import *

class Solution(object):
# ------------------------Your Solution in here-----------------------------------------------
    def duplicates(self, nums):

        pass


# --------------------------------------------------------------------------------------------
#                   The function should return a boolean (True/False)


def solution_testings():
    _ = Solution()
    for nums, answer in duplicates_list:
        print(f"testing nums {nums} for duplicates")
        res = _.duplicates(nums)
        if res == answer:
            print(f"function passed!")
        else:
            raise Exception(f"Your function returned {res}, which results should be {answer}")
    print("*"*25)
    print("You Did it!")
    print("*" * 25)

if __name__ == '__main__':
    solution_testings()

