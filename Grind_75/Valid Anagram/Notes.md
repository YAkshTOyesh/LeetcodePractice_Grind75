# UMPIRE
## Understand
### Explanation
Check if anagram. Are letters in t the same count as letters in s.

### Algo:
Create a hashmap of frequency letters for s - O(N) for space
Loop through t and keep checking and decrementing counts
if loop finishes return true
else return false (count 0 or not in)


### Test Cases
s = 'bad' , t = 'dad'
s = 'b a d', t = 'd  ab' Return True


### Edge Cases
s ='' t ='' - return True. Algo handles that
s =' t = 'a' - return False
Blank spaces and "," - Algo handles that 
Duplicated letters - Algo handles that
s ='aaaa' , t ='a' - Return False

### Constraints
```python
"""
< 10 - O(N!)
< 20 - O(2^N)
< 10^3 - O(N^3)
< 10^4 - O(N^2)
< 10^5 - O(NlogN)
< 10^6 - O(N)
> 10^6 - O(logN), O(1)
"""
```

Use letters exactly once.
Input <= 5 * 10^4 O(NlogN), O(N), O(logN), O(1)

## Match

### Potential Data Operations per element
Count frequency of element - O(N)
Search if element exists - O(1)
Decrement/Delete element - O(1)
Loop - O(N)


### Potential Algorithms
Loop


### Potential Data Structures
Hashmap - O(N)

## Plan
```python
"""
Pseudocode
INITIALIZE empty frequency_map = {}
FOR char IN s:
    CHECK IF char IN frequency_map:
        ADD char TO frequency_map
        INITIALIZE a count = 0
        {char : count}
    INCREMENT its count by += 1
FOR char IN t:
    CHECK IF char IN frequency_map (look for the key)
        CHECK IF its count == 0
            # Used all letters not anagram
            RETURN False 
        DECREMENT count by -= 1
    ELSE:
        RETURN False
ALL words used up
CHECK IF frequency map IS EMPTY:
    RETURN False
ELSE:
    RETURN True
"""
```
## Implement
```python
"""
Include print statements
"""
print('Program starts here.')
frequency_map = {}
print('Creating frequency map for string: ' + str(s))
for char in s:
    if char not in frequency_map:
        frequency_map[char] = 0
    frequency_map[char] += 1
print("Frequency map is: " + str(frequency_map))
for char in t:
    print('    ---START---')
    print('    Looking for character "' + str(char) + '" in frequency map')
    if char in frequency_map: # (look for the key)
        print('        Yes. Letters are available decrement by 1.')
        frequency_map[char] -= 1
    else:
        print('        No. Letter is not even in frequency_map')
        print('        Returning False. Not an anagram.')
        return False
    if frequency_map[char] == 0:
            # Used all letters not anagram
            print('        Deleting from frequency_map')
            del frequency_map[char]
    print('    Moving up to the next character.')
    print('    ---END---')
    print()
print('Checking if frequency map is not empty')
print('Making sure s is not a subset of t')
if frequency_map:
    print('    Elements exist in frequency_map')
    print('    Not an anagram')
    return False
else:
    print('    Frequency map is empty')
    print('    Valid Anagram')
    return True
```
## Review

Manual walkthrough with right example
BUD - Bottlenecks, Unnecesssary work, Duplicated work
Example s ='bad', t ='dad'
Looks good. O(N) - Time, O(N) - Space

## Explain

Time Complexity - O(N)
Space Complexity - O(N)
 