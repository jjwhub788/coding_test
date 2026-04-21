class Solution {
    public int[] solution(int n) {
        //n 이하의 홀수의 개수 
      int size = (n + 1) / 2;     
        int[] answer = new int[size];
        
        int num = 1;
        
        for (int i = 0; i < size; i++) {
            answer[i] = num;
            num += 2;
        }
        
        return answer;
    }
}