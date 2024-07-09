# UMPIRE
# Understand
## Explanation
I have an array nums and a target. I have to find num[i] + num[j] = target, 
where num[i] and num[j]are unique. I have to return i and j\
CANNOT SORT - I have to maintain the index.\
I have to search for something very quickly.\
Create a Hashmap.\ 
For each num: calculate num to find target - num: if in Hashmap then index found.\
Return both indices.\


## Test Cases
* [1,4,6,7,8,10,11,20], tagrget = 10 - returns [1,2]
* [9,1,8], taregt = 9 - returns [1,2]


## Edge cases
* Empty array [] - return ???
* Negative values ??? Yes. Note answer is unique !!!

## Constraints
Inputs < 10 - O(n!)\
Inputs < 20 - O(2^N) - recursion???\
Inputs < 10^3 - O(N^3)\
Inputs < 10^4 - O(N^2)\
Inputs < 10^5 - O(NlogN)\
Inputs< 10^6 - O(N)\
Inputs > 10^6 - O(1), O(logN)\

Order does not matter\
Exactly 1 solution\
Do not use same element twice. Cannot happen since ans is unique.\
E.g 8 - 4 = 4. Only 2 numbers given. Hashmap does NOT handle that.\ 
Can use [4,4] Same value BUT different index [0,1]\
However [4] and then return [0,0] for target = 8 (4 +4)\ Error !!!\
Inputs: < 10^4 (min O(N^2))\
Do better than O(N^2) !!!!\

# Match
## Data Operations performed per element:
Searching for an element very fast - O(1)\

## Potential Algorithms:
Loop ???\

## Potential Data Structure
Hashmap/Dictionnary\

# Plan

## Pseudocode
```python
"""
INITIALIZE empty_hashmap = {}
FOR index IN range(0, len(nums)):
    value = nums[index]
    empty_hashmap[value] = index
INITIALIZE target_is_not found = True
INITIALIZE answer = []
WHILE target_is_not_found:
    FOR index IN range(0, len(nums)):
        tagret_num_to_find = target - num
        IF target_num_to_find IN empty_hashmap:
            target_is_not_found = False
            answer.append(index)
            answer.append(empty_hashmap[target_num_to_find])
            RETURN answer
        ELSE DO NOTHING, KEEP LOOKING
PRINT('Error !')
"""
```
# Implement 
```python
# Include print statements
def twoSum(self, nums: List[int], target: int) -> List[int]:
  print('----Program Starts Here.----')
  hashmap_num = {}

  # Fill hashmap with {value : index}
  for index in range(0, len(nums)):\
      value = nums[index]\
      hashmap_num[value] = index\
  answer_res = []\
  print('Hashmap contains: ' + str(hashmap_num))

  for index in range(0, len(nums)):
      print('-----START-----')
      print('    Looking for a pair with the number: ' + str(nums[index]))
      target_num_to_find = target - nums[index]
      print('    Target num to find is: ' + str(target_num_to_find))
      if target_num_to_find in hashmap_num and hashmap_num[target_num_to_find] != index:
          print('        Yes! Pair found')
          answer_res.append(index)
          answer_res.append(hashmap_num[target_num_to_find])
          print('Returning the answer: ' + str(answer_res))
          return answer_res
      print('-----END-----')
      print()

```

# Review
  """\
  Time Complexity - O(N)\
  Space Complexity - O(N)\
  """