from auto_test import *

class Solution(object):
# ------------------------Your Solution in here-----------------------------------------------
    def ispalindrome(self, x: int) -> bool: # DO NOT CHANGE THIS LINE












# --------------------------------------------------------------------------------------------



def solution_testings():
    _ = Solution()
    for num, answer in palindrome_dict.items():
        if answer == _.ispalindrome(num):
            pass
        else:
            print(f"{num} should be {answer} but got {_.ispalindrome(num)}")





if __name__ == '__main__':
    solution_testings()

