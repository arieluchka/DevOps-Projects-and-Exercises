## Two Sum
Given an array of integers `nums` and an integer `target`, return a list of two integers, that represent the index of the nums that add up to the `target`.

Write your code in the "twoSum" function. The function should return **a list of the two indexes of the list `nums`** 

**Run the file main.py to test your code.**

## Examples:
### Example 1:
**Input**: nums = [2,7,11,15], target = 9

**Output**: [0,1]

**Explanation**: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
**Input**: nums = [3,2,4], target = 6

**Output**: [1,2]


### Example 3:
**Input**: nums = [3,3], target = 6

**Output**: [0,1]


---
<details>
  <summary>Hint 1</summary>

    A really brute force way would be to search for all possible pairs of numbers.
  
</details>

<details>
  <summary>Hint 2</summary>

    if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is target - x.
    example: 
    input: nums = [3,2,4], target = 6
    x = 3
    6 - 3 == y = 3, so we search for another number in the nums list, containing 3.
    x = 2 
    6 - 2 == y = 4, so we search and find 4, the last number in the list nums!

  
</details>
