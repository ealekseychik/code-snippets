# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char == ')':
                queue = []
                while stack and stack[-1] != '(':
                    queue.append(stack.pop())

                if stack:
                    stack.pop()

                stack.extend(queue)
            else:
                stack.append(char)
        
        return ''.join(stack)
