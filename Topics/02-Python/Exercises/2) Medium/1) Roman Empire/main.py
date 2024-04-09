from auto_test import *

class Solution(object):
# ------------------------Your Solution in here-----------------------------------------------
    def roman_to_int(self, roman_number):




# --------------------------------------------------------------------------------------------
#                   The function should return an integer


def solution_testings():
    _ = Solution()
    for roman_str, roman_int in roman_to_int_list:
        print(f"converting the roman number {roman_str} to int")
        if _.roman_to_int(roman_str) == roman_int:
            print(f"function passed! {roman_str} == {_.roman_to_int((roman_str))}\n")
        else:
            raise Exception(f"Your function returned {_.roman_to_int(roman_str)} but the correct answer is {roman_int}")
    print("*"*25)
    print("You Did it!")
    print("*" * 25)

if __name__ == '__main__':
    solution_testings()

