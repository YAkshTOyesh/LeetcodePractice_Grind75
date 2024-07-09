def twoSum(self, nums: List[int], target: int) -> List[int]:
  prevMap = {} # value : index

  for index, num in enumerate(nums):
    target_num_to_find = target - num
    if target_num_to_find in prevMap:
      return [prevMap[target_num_to_find], index]
    prevMap[num] = index

  """
  An important lesson. Hashmap is used to see if an element exists. Concept of mapping. A unique solution to something.
  """