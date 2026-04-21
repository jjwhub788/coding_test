class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int max = 0;
        int[] count = new int[1001]; 

        for (int i = 0; i < array.length; i++) {
            count[array[i]]++;
        }

        for (int i = 0; i < count.length; i++) {
            if (count[i] > max) {
                max = count[i];
                answer = i;
            } else if (count[i] == max) {
                answer = -1;
            }
        }
        return answer;
    }
}