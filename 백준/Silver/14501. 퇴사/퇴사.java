import java.util.*;
import java.io.*;

public class Main {
	
	static int N;
	static int[] T;
	static int[] P;
	

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		T = new int[N+1];
		P = new int[N+1];
		int [] dp = new int[N+2];
		
		// T: 상담을 완료하는 데 걸리는 기간
		// P: 상담을 했을 때 받을 수 있는 금액
		for(int i = 1; i< N+1; i++) {
			StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
			T[i] = Integer.parseInt(stk.nextToken());
			P[i] = Integer.parseInt(stk.nextToken());
		}
		
		for (int i = N; i >= 1; i--) {
			if (i+T[i] <= N+1) {
				dp[i] = Math.max(dp[i+1], dp[i+T[i]] + P[i]);
			}else {
				dp[i] = dp[i+1];
			}
			
		}
		System.out.println(dp[1]);
	}
}
