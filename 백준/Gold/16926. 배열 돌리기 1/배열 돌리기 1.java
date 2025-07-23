import java.io.*;
import java.util.*;

public class Main {
	static int N, M, R;
	static int[][] arr;
	static int min;
	
	static int[] dr = {0,1,0,-1};
	static int[] dc = {1,0,-1,0};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		R = Integer.parseInt(stk.nextToken());
		
		arr = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine()," ");
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
		
		min = Math.min(N, M);
		for (int i = 0; i < R; i++) {
			rotate();
		}
		print();
	}
	
	public static void print() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	// i, j든 인덱스가 끝값이면 바뀌나봐
	public static void rotate() {
		
		for (int t = 0; t < min/2; t++) {
				int x = t;
				int y = t;
				int temp = arr[t][t];
				
				int idx = 0;
				while (idx <=3) {
					int nx = x+dr[idx];
					int ny = y+dc[idx];
					if (t<=nx && t<= ny && N-t>nx && M-t>ny) {
						arr[x][y] = arr[nx][ny];
						x = nx;
						y = ny;
					}else {
						idx++;
					}
				}
				arr[t+1][t] = temp;
		}
	}
}