import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        
        Arrays.sort(numbers);
        int n = numbers.length;
        
        // 가장 큰 두 수 곱
        int max1 = numbers[n - 1] * numbers[n - 2];

        return max1;
    }
}