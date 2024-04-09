from auto_test import *

class Solution(object):
# ------------------------Your Solution in here-----------------------------------------------
    def ispalindrome(self, num):




# --------------------------------------------------------------------------------------------
#                   The function should return a boolean (True/False)


def solution_testings():
    _ = Solution()
    for num, answer in palindrome_dict.items():
        print(f"testing num {num}")
        if answer == _.ispalindrome(num):
            print(f"num {num} passed!\n")
        else:
            raise Exception(f"{num} should be {answer} but got {_.ispalindrome(num)}")
    print("*"*25)
    print("You Did it!")
    print("*" * 25)

if __name__ == '__main__':
    solution_testings()

