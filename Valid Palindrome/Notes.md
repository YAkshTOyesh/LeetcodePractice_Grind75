# UMPIRE
## Understand
Explanation
Read the same backwards and foward. Use two pointers. But do some 
cleaning first.
converting all uppercase letters into lowercase letters
emoving all non-alphanumeric characters.
Alphanumeric characters include letters and numbers.
Use a hashmap to store alphanumeric characters.
If not in hashmap move the pointer until correct then check.
Keeping checking until pointers cross.
Return true
If cross fails return false.

## Test Cases
"aba" - returns True
"1a2a1" - returns True
"A11A" - returns True
"A 1 A" returns True (space character not in hashmap)
"A               ,,,,:'''A         " - returns True (not in hasmap)


## Edge Cases
" " - returns True (not in hashmap I guess????)
Pointers out of bounds ????
"" - returns True
"A" - Cross condition ??? == or "AA" while left < right


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

I may need O(NlogN or O(N))

# Match

## Potential Data Operations per element
Check if alphanumeric - O(1) (Hashmap)  
Do .lower() - O(1) (In built)  
Move pointer - O(1)  


## Potential Algorithms
Loop - O(N)


## Potential Data Structures
Hashmaps
Pointers

# Plan
```python
"""
Pseudocode
INITIALIZE alpha_numeric_hashmap
CONVERT s TO LOWER()
INITIALIZE left_pointer = 0
INITIALIZE right_pointer = len(s)
WHILE left_pointer <= right_pointer:
    CHECK IF s[left_pointer] NOT IN alpha_numeric_hashmap:
        INCREMENT left_pointer += 1
    CHECK IF s[right_pointer] NOT IN alpha_numeric_hashmap:
        DECREMENT right_pointer -= 1
    # Try reading forward and backward. Check if valid palindrome
    CHECK IF s[left_pointer] != s[right_pointer]:
        RETURN False
    # Move pointers for next character
    INCREMENT left_pointer += 1
    DECREMENT right_pointer -= 1
# Looks like word is a valid palindrome
RETURN True
"""
```
# Implement
```python
"""
Include print statements
"""
print('Program starts here.')
alpha_numeric_set = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1',
                        '2', '3', '4', '5', '6', '7', '8', '9', '0')
s_lower = s.lower()
print(s_lower)
left_pointer = 0
right_pointer = len(s) - 1
while left_pointer < right_pointer:
    print('    ---START---')
    # Keep moving until
    while s_lower[left_pointer] not in alpha_numeric_set and left_pointer < right_pointer:
        print('        Character is: "' + str(s_lower[left_pointer]) + '"')
        left_pointer += 1
        print('        Left Pointer is now: ' + str(left_pointer))
    # Keep moving until
    while s_lower[right_pointer] not in alpha_numeric_set and left_pointer < right_pointer:
        print('        Character is: "' + str(s_lower[right_pointer]) + '"')
        right_pointer -= 1
        print('        Left Pointer is now: ' + str(left_pointer))
    # Try reading forward and backward. Check if valid palindrome
    print('    Left pointer is: ' + str(left_pointer))
    print('    Right pointer is: ' + str(right_pointer))
    print('    Left_character is: '+ str(s_lower[left_pointer]))
    print('    Right_character is: '+ str(s_lower[right_pointer]))
    if s_lower[left_pointer] != s_lower[right_pointer]:
        print('        Invalid Palindrome')
        return False
    # Move pointers for next character
    left_pointer += 1
    right_pointer -= 1
    print('    ---END---')
    print()
# Looks like word is a valid palindrome
print('Valid Palindrome')
return True
```
# Review

* Time Complexity - O(N) Worst case is O(N/2) which is O(N)
* Space Complexity - O(1) - Constant 36 characters


