class Solution {
    public boolean judgeCircle(String moves) {
        int up = 0;
        int left = 0;
        for (int i = 0; i < moves.length(); i ++) {
            char c = moves.charAt(i);
            if (c == 'U') {
                up += 1;
            } else if (c == 'D') {
                up -= 1;
            } else if (c == 'L') {
                left += 1;
            } else if (c == 'R') {
                left -= 1;
            }
        }
        
        if (up == 0 && left == 0) return true;
        return false;        
    }
}