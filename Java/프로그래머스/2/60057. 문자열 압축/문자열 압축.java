import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(String s) {
        //예외처리 : 길이가 1이면 압축할 필요 없음
        if(s.length()==1){
            return 1;
        }
        
        //가장 짧은 압푹 문자열 길이 저장
        int answer = s.length();
        
        //일정한 크기로 다 나눠보기 
        for(int divd = 1; divd<= s.length()/2; divd++){
            StringBuilder compressed = new StringBuilder();
            
            //첫번째 문자열 기준(top)
            String prev = s.substring(0, divd);
            int count = 1;
            
            //현재 문자열 순회
            for (int i=divd; i<s.length(); i+=divd){
                //마지막 남은 문자열 처리
                int end = Math.min(i+divd, s.length());
                
                String cur = s.substring(i, end);
                
                //스택의 top과 현재(cur)와 비교
                if(prev.equals(cur)){
                    //같다면 top 중복 개수 증가 시키기
                    count ++;
                } else{
                    //다르면 cur, 1 push
                    if(count>1){
                        compressed.append(count);
                    }
                    //문자열 추가
                    compressed.append(prev);
                    //새로운 문자열을 위로 올리기
                    prev = cur;
                    //개수 초기화
                    count =1;
                }
            }
            //마지막 남아있는 문자열 처리
            if(count>1){
                compressed.append(count);
            }
            compressed.append(prev);
            //길이 비교 후 최소 길이를 업데이트
            answer = Math.min(answer, compressed.length());
        }
        //가장 짧은 압축 문자열의 길이를 반환한다.
        return answer;
    }
}