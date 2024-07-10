# UMPIRE
# Understand
## Explanation
I have to find if it is valid. I start with 1st bracket in string.
Search for next bracket to close it. Keep going until an error. Use a stack 

Creating a hashmap for mapping corresponding brackets in O(1)
Deal with open brackets only !!!!
Add to stack. 
Once you see a close try to pop off.
If no popping, leads to out of order + cannot reduce stack, thus false
Else True until end of string reached.


## Test cases
* "{{{(([[]]))}}}" - return True
* "((((]]]](((" - return False (not same type)
* "((((]]]][[[[))))" - return False (not correct order)
* "()()(" - return False (no corresponding)


## Edge cases
* Empty string - return False
* "(" - return False
* ")" - return False


## Constraints
```python
"""
< 10 - O(N!)
< 20 - O(2^N)
< 10^3 - O(N^3)
< 10^4 - O(N^2)
< 10^5 - O(NlogN)
< 10^6 - O(N)
> 10^6 - O(1), O(logN)
"""
```

Slowest Algo is O(N^2), Can you do faster?
An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every close bracket has a corresponding open bracket of the same type.

# Match

## Potential Data Operations:
Map each type of brackets - O(1), Space O(1) [upper bound is constant 3]
Add each open brackets to stack - O(1), Space O(N)
Pop each open brack - O(1), Space O(N)


## Potential Algorithms
Loop, Stack, Hashmap


## Potential Data Structures
Hashmap + Stack

# Plan
```python
"""
Pseudocode
INITIALIZE brackets_hashmap
INITIALIZE open_brackets_stack
FOR bracket in s:
    # Check if an open bracket
    if bracket in brackets_hashmap:
        ADD TO open_brackets_stack.append(bracket)
    else:
        ACCESS TOP OF open_brackets_stack
        corresponding_bracket = open_brackets_stack[-1]
        if corresponding_bracket == bracket:
            POP open_brackets_stack.pop()
        else:
            RETURN False
RETURN True
"""
```
# Implement
```python
"""
Include print statements
"""
# print('Program starts here.')
brackets_hashmap = {"(" : ")", "[" : "]", "{" : "}"}
open_brackets_stack = []
for bracket in s:
    # Check if an open bracket
    # print('    ---START---')
    # print('    Checking validity for bracket: ' + str(bracket))
    if bracket in brackets_hashmap:
        # print('        Yes! An open bracket. Add it to stack.')
        open_brackets_stack.append(bracket)
        # print('        Open bracket stack currently is: ' + str(open_brackets_stack))
    else:
        # print('        No! This is a close bracket')
        if len(open_brackets_stack) == 0:
            # print('            Stack is empty cannot cancel the open bracket')
            return False
        # ACCESS TOP OF open_brackets_stack
        corresponding_bracket = open_brackets_stack[-1]
        # print('        Checking if close bracket can close off last seen open bracket')
        if brackets_hashmap[corresponding_bracket] == bracket:
            # print('            Yes! Pop the stack')
            open_brackets_stack.pop()
            # print('            Stack currently is: ' + str(open_brackets_stack))
        else:
            # print('            No! Bracket cannot close. It is in valid.')
            return False
    # print('    Valid. Moving to next bracket')
    # print('    ---END---')
    # print()
if len(open_brackets_stack) != 0:
    # print('Not all open brackets were popped off.')
    return False
return True
```
# Review

Time Complexity - O(N)
Space Complexity - O(N)
