class Solution:
    def isValid(self, s: str) -> bool:
        print('Program starts here.')
        brackets_hashmap = {"(" : ")", "[" : "]", "{" : "}"}
        open_brackets_stack = []
        for bracket in s:
             # Check if an open bracket
            print('    ---START---')
            print('    Checking validity for bracket: ' + str(bracket))
            if bracket in brackets_hashmap:
                print('        Yes! An open bracket. Add it to stack.')
                open_brackets_stack.append(bracket)
                print('        Open bracket stack currently is: ' + str(open_brackets_stack))
            else:
                print('        No! This is a close bracket')
                if len(open_brackets_stack) == 0:
                    print('            Stack is empty cannot cancel the open bracket')
                    return False
                 # ACCESS TOP OF open_brackets_stack
                corresponding_bracket = open_brackets_stack[-1]
                print('        Checking if close bracket can close off last seen open bracket')
                if brackets_hashmap[corresponding_bracket] == bracket:
                    print('            Yes! Pop the stack')
                    open_brackets_stack.pop()
                    print('            Stack currently is: ' + str(open_brackets_stack))
                else:
                    print('            No! Bracket cannot close. It is in valid.')
                    return False
            print('    Valid. Moving to next bracket')
            print('    ---END---')
            print()
        if len(open_brackets_stack) != 0:
            print('Not all open brackets were popped off.')
            return False
        return True