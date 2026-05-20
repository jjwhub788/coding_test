class Solution {
    public int solution(int[] numbers, int k) {
        
        // 공은 한 명 건너뛰고 던지므로 +2칸씩 이동
        // 배열은 0부터 시작하니까 (k-1)
        
        int index = (2 * (k - 1)) % numbers.length;
        return numbers[index];
    }
}