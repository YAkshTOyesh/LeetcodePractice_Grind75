# UMPIRE
## Understand
Explanation
I have 2 LINKED LIST. Both are SORTED in ASC. Merge both so that res_linked_list is
in ASC.

I can do it in place !!!

## Test Cases
L1 -  1 -> 4 
L2 - 0
Returns L3 -  0 -> 1 -> 4

## Edge Cases
Empty L1 ??? If None then skip??? Return empty
Equal values next to each other

## Constraints
```python
< 10 - O(N!)
< 20 - O(2^N)
< 10^3 -  O(N^3)
< 10^4 - O(N^2)
< 10^5 - O(NlogN)
< 10^6 -  O(N)
> 10^6 - O(1), O(logN)
```

The number of nodes in both lists is in the range [0, 50].
    Can use O(N^3) ????
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
    Can do a step by step traversing.

# Match

## Potential Data Operations per element
Insert in Linked List -  O(1) Do an append
Traverse element in linked list - O(1), O(N)

## Potential Algorithms
Loop - O(N)

## Potential Data Strucutures
Linked list

# Plan

## Pseudocode
```python
current1 = list1
current2 = list2
if list1.val <= list2.val:
    head_merged_lsit = list1
else:
    head_merged_list = list2
WHILE current1.next IS NOT None:
    IF current1.next > current2:
        # Hold on its next before merging
        temp_linked_list = current1.next
        # DO the merging
        current1.next = current2
        # Update current2 to temp
        # current1 is moving in the second list now (alternating)
        current2 = temp
    # Move current pointer to the next objecct in the list
    current1 = current1.next
RETURN head_merged_list
"""
```
# Implement
```python
"""
Include print statements
"""
print('Program starts here.')
current1 = list1
current2 = list2
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
origin1 = list1
origin2 = list2
print('Merged List currently is: ')
print(self.to_print(head_merged_list))
while start_list.next is not None:
    print('    ---START---')
    print('    Current head is at: ' + str(start_list.val) + ' at ' + current_list)
    print('    Merged List currently is: ')
    print('    ' + self.to_print(head_merged_list))
    if start_list.next.val >= alternate_list.val:
        print('        Changing Lists')
        if current_list == 'list1':
            current_list = 'list2'
        else:
            current_list = 'list1'
        # Hold on its next before merging
        temp_linked_list = start_list.next
        # DO the merging
        start_list.next = alternate_list
        # Update current2 to temp
        # current1 is moving in the second list now (alternating)
        alternate_list = temp_linked_list
    # Move current pointer to the next objecct in the list
    start_list = start_list.next
    # print('    Merged List currently is: ')
    # print('    ' + self.to_print(head_merged_list))
    print('    ---END---')
    print()
start_list.next = alternate_list
print(self.to_print(head_merged_list))
return head_merged_list
```
# Review
Time Complexity - O(N)
Space Complexity - O(1)
