class Solution {
    public String solution(int age) {
        String answer = "";
        String str = String.valueOf(age);  // 숫자를 문자열로 변환
        for (int i = 0; i < str.length(); i++) {
            int num = str.charAt(i) - '0';   // 문자 → 숫자 변환
            answer += (char) (num + 'a');    // 숫자 → 알파벳 변환
        }
        return answer;
    }
}