from two_num_sum import TwoNumSumSlowTest
from two_num_sum import TwoNumSumFastTest

def testTrueOrFalse(twoNumSum, trueOrFalse, vals):
    for val in vals:
        assert twoNumSum.test(val) is trueOrFalse

test1 = [1, -2, 3, 6]
trues = [4, -1, 9]
falses = [10, 5, 0]

slow = TwoNumSumSlowTest()
slow.store_multiple(test1)

testTrueOrFalse(slow, True, trues)
testTrueOrFalse(slow, False, falses)

fast = TwoNumSumFastTest()
fast.store_multiple(test1)

testTrueOrFalse(slow, True, trues)
testTrueOrFalse(slow, False, falses)

print("Testing: GOOD")
