def longestValidParentheses(s: str) -> int:
    stack = [-1]
    max_len = 0

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len
s = input("Enter the parentheses string: ")
print("Longest Valid Parentheses Length:", longestValidParentheses(s))
