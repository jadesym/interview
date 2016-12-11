import re

test_cases = {
    '3.0': True,
    '2': True,
    'e': False,
    '-2': True,
    '3.A': False,
    None: False,
    '+5.123': True,
    '': False,
    '.': False,
    '+.': False,
    '-.': False,
    '+': False,
    '-': False
}

def isNumber(string):
    if string is None: return False
    return re.fullmatch("[+-]?\d+\.?\d*", string) is not None

for test_case in test_cases:
    print(test_case, isNumber(test_case), test_cases[test_case])
    assert isNumber(test_case) is test_cases[test_case]
