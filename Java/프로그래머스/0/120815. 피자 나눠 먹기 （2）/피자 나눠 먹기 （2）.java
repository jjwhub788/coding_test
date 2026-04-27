class Solution {
    public int solution(int n) {
        int lcm = lcm(6, n);
        return lcm / 6;
    }

    // 최대공약수
    public int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    // 최소공배수
    public int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
}