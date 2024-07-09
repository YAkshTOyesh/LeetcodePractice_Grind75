def twoSum(self, nums: List[int], target: int) -> List[int]:
  print('----Program Starts Here.----')
  hashmap_num = {}

  # Fill hashmap with {value : index}
  for index in range(0, len(nums)):
      value = nums[index]
      hashmap_num[value] = index
  answer_res = []
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

  # Review
  """
  Time Complexity - O(N)
  Space Complexity - O(N)
  """

