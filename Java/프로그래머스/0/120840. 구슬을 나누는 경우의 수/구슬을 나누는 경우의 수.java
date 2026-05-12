class Solution {
    public long solution(int balls, int share) {
        
        if (share > balls) return 0;
        if (share == 0 || share == balls) return 1;
        
        long answer = 1;
        
        for (int i = 0; i < share; i++) {
            answer = answer * (balls - i) / (i + 1);
        }
        
        return answer;
    }
}