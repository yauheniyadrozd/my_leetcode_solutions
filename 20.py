class Solution:
    def isValid(self, s: str) -> bool:
        begin = []
        map = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i not in map:
                begin.append(i)
            else:
               if not begin or begin.pop() != map[i]:
                    return False

        return not begin