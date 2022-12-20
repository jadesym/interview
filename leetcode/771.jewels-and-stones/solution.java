class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> stones = new HashSet<>();

        for (int i = 0; i < J.length(); i++){
            char c = J.charAt(i);
            stones.add(c);
        }

        int jewelCount = 0;
        for (int j = 0; j < S.length(); j++) {
            char c = S.charAt(j);
            if (stones.contains(c)) {
                jewelCount++;
            }
        }
        return jewelCount;
    }
}