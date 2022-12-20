class Solution {
    public boolean isSelfDividing(int x) {
        int currentVal = x;
        while (currentVal > 0) {
            int currentDigit = currentVal % 10;
            if (currentDigit == 0 || x % currentDigit != 0) {
                return false;
            }
            currentVal /= 10;
        }
        return true;
    }

    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> nums = new ArrayList<>();
        for (int x = left; x < right + 1; x++) {
            if (isSelfDividing(x)) {
                nums.add(x);
            }
        }
        return nums;
    }
}