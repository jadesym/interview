class Solution {
    public int findComplement(int num) {
        int numCopy = num;
        int complement = 0;
        int currentIndex = 0;
        while (numCopy > 0) {
            int curDigit = numCopy % 2;

            if (curDigit == 0) {
                complement += Math.pow(2, currentIndex);            
            }

            currentIndex++;
            numCopy /= 2;
        }

        return complement;
    }
}