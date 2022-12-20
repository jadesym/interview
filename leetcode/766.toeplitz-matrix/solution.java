class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int height = matrix.length;
        int width = matrix[0].length;
        
        for (int row = 0; row < height; row++) {
            int col = 0;
            if (!isSameDiag(matrix, row, col, height, width)) {
                return false;
            }
        }        

        for (int col = 1; col < width; col++) {
            int row = 0;
            if (!isSameDiag(matrix, row, col, height, width)) {
                return false;
            }
        }

        return true;
    }

    public boolean isSameDiag(int[][] matrix, int row, int col, int height, int width) {
        int currentDiagVal = matrix[row][col];
        for (int i = 1; i < Math.min(height - row, width - col); i++) {
            int curRow = (row + i) % height;
            int curCol = (col + i) % width;
            if (currentDiagVal != matrix[curRow][curCol]) {
                return false;
            }      
        }
        return true;
    }
}