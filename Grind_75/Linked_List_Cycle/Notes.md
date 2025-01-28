
# UMPIRE  
## Understand  

### Explanation  
Due to the constraint, O(N^2) or less. Potentially O(1). Use a fast pointer and a slow pointer. Start at the same place. Fast poiner will have twice the speed of slow pointer, then if a cycle exists it "reduces the speed of the fast pointer" where fast pointer gets behind and will always catch up or cross slow pointer again. Think of cars. If no crossing ever happens terminate. Terminate when end of list is reached.

### Algorithm Loop Invariant.  
Before next iteration, slow and fast have not met yet. After next iteration, fast or slow have not met or one of them probably fast will reach the end.
Initialization; Beggining
Termination: end of list

### Test Cases

**3 Long Happy Case -**
(3) -> (2) -> (4) -> (8) -(7) -> (9) - back to -> (2) = return True  
(3) -> (2) -> (4) - back to -> (2) = return True  
(3) -> (2) -> (0) -> (-4) -> (5) - back to (2) = return True  
**1 Bad Case -**
(3) -> (2) -> (6) -> (8) -> end = return False  
**1 Edge Case (very small or zero or at the end) -**   
(3) = return False  
NULL = return False  
(3) -> (2) -> back to (3) - return True  
(3) -> (2) -> (4) -> (6) - back to -> (4) - return True (small loop at the end) 

### Constraints
```python
"""
< 10 - O(N!)
< 10^2 -  O(2^N)
< 10^3 - O(N^3)
< 10^4 - O(N^2)
< 10^5 - O(NlogN)
< 10^6 - O(N)
> 10^6 - O(1)
"""
```

## Match
### Potential Data Operations per element
Check if fast pointer and slow pointer are pointing at the same node.

### Potential Data Structures
Linked Lists and Pointers
### Potential Algorithms
Fast and Slow Pointers
Cheatsheet says: Fast and Slow Pointers

## Plan
```python
"""
Write in Pseudocode.
INITIALIZE fast_pointer = head
INITIALIZE slow_pointer = head
//While end of list is not reached by fast pointer or cycle found continue looping
WHILE fast_pointer IS NOT None AND fast_pointer.next IS NOT None:
     fast_pointer = fast_pointer.next.next // Move fast pointer. Can through NULL error if .next is null
     slow_pointer = slow_pointer.next
     If fast_pointer = slow_pointer: //Does it point at same obj?
        RETURN True
// End of list reached
RETURN False
    
"""
```

## Implement
```python
# """
# Include print statements. Space +4 recursive
# """
fast_pointer = head
slow_pointer = head
while fast_pointer is not None and fast_pointer.next is not None:
    fast_pointer = fast_pointer.next.next
    slow_pointer = slow_pointer.next
    if fast_pointer == slow_pointer:
        return True
return False
```

## Review
Trace Testing  
BUD - Bottlenecks, Unecessary work, repeated work  
Looks Good!  

## Explain

Time Complexity - O(N) will loop through all elements at most even if cycle is very big and far away.  
Space Complexity - O(1) No extra memory used

