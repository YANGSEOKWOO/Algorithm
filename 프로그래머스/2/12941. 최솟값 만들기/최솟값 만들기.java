// 뭐가 최적일까?
import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(B);
        Arrays.sort(A);
        
        for(int i = 0; i < B.length; i++){
            answer += A[i]*B[B.length-i-1];
        }

        return answer;
    }
}