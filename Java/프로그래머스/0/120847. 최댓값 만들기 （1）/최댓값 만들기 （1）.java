import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        
        Arrays.sort(numbers);
        int n = numbers.length;
        
        // 가장 큰 두 수 곱
        int max1 = numbers[n - 1] * numbers[n - 2];
        
        // 가장 작은 두 수 곱 (음수 × 음수 가능성)
        int max2 = numbers[0] * numbers[1];
        return Math.max(max1, max2);
    }
}