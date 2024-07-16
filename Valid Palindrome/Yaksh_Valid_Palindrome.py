class Solution:
    def isPalindrome(self, s: str) -> bool:
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