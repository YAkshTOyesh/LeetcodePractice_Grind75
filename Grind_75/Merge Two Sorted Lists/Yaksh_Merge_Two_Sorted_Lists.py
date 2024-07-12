# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def to_print(self, linked_lst):
      curr = linked_lst
      string_to_print = ''
      while curr is not None:
          string_to_print += str(curr.val) + ' -> '
          curr = curr.next
      string_to_print += 'None'
      return string_to_print

  def mergeTwoLists(self, list1, list2):
      print('Program starts here.')
      if list1 is None and list2 is None:
          return None
      if list1 is None and list2 is not None:
          return list2
      if list1 is not None and list2 is None:
          return list1
      if list1.val <= list2.val:
          head_merged_list = list1
          start_list = list1
          alternate_list = list2
          current_list = 'list1'
      else:
          head_merged_list = list2
          start_list = list2
          alternate_list = list1
          current_list = 'list2'
      print('Merged List currently is: ')
      print(self.to_print(head_merged_list))
      while start_list.next is not None:
          print('    ---START---')
          print('    Current head is at: ' + str(start_list.val) + ' at ' + current_list)
          print('    Merged List currently is: ')
          print('    ' + self.to_print(head_merged_list))
          if start_list.next.val >= alternate_list.val:
              print('        Changing Lists')
              current_list = 'list2' if current_list == 'list1' else 'list1'
              # Hold on its next before merging
              temp_linked_list = start_list.next
              # DO the merging
              start_list.next = alternate_list
              # Update current2 to temp
              # current1 is moving in the second list now (alternating)
              alternate_list = temp_linked_list
          # Move current pointer to the next objecct in the list
          start_list = start_list.next
          print('    ---END---')
          print()
      start_list.next = alternate_list
      print(self.to_print(head_merged_list))
      return head_merged_list