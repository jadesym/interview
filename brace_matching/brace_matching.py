"""
/**
 * This function determines if the braces ('(' and ')') in a string are properly matched.
 * it ignores non-brace characters.
 * Some examples:
 * "()()()()" : True
 * "((45+)*a3)" : True
 * "(((())())" : False
 * ")(" : False
 * "))((" : False
 * "()0" : True
 * "))" : True
 */
"""

test_cases = {
    "()()()()" : True,
    "((45+)*a3)" : True,
    "(((())())" : False,
    ")(" : False,
    "))((" : False,
    "()0" : True,
    "))" : False
}

def brace_matching(a):
    braceCount = 0
    for char in a:
        if char == "(":
            braceCount += 1
        elif char == ")":
            braceCount -= 1
        if braceCount < 0: return False
    return braceCount == 0

for case in test_cases:
    assert test_cases[case] is brace_matching(case)
print("Working...")
