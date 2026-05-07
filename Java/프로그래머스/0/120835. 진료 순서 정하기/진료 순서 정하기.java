import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        int[] sorted = emergency.clone(); // 원본 복사

        Arrays.sort(sorted); // 오름차순 정렬

        for (int i = 0; i < emergency.length; i++) {
            for (int j = 0; j < sorted.length; j++) {
                if (emergency[i] == sorted[j]) {
                    answer[i] = sorted.length - j; // 순위 계산
                }
            }
        }

        return answer;
    }
}