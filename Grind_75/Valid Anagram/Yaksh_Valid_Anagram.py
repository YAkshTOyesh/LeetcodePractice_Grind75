class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
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