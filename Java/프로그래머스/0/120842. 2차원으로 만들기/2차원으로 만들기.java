class Solution {
    public int[][] solution(int[] num_list, int n) {
        
        // 행 개수
        int rows = num_list.length / n;
        
        // 2차원 배열 생성
        int[][] answer = new int[rows][n];
        
        int idx = 0;
        
        // 2차원 배열 채우기
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < n; j++) {
                answer[i][j] = num_list[idx];
                idx++;
            }
        }
        
        return answer;
    }
}