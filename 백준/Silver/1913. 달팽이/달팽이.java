import java.io.*;

public class Main {
	static int N;
	static int findNum;
	static int[][] snailRoad;
	static int r, c, dir, x, y;
	
	static int[] dr = {1,0,-1,0};
	static int[] dc = {0,1,0,-1};
	
	
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		findNum = Integer.parseInt(br.readLine());
		
		snailRoad = new int[N][N];
		
		for (int i = N*N; i > 0; i--) {
			snailRoad[r][c] = i;
			
			int nr = r + dr[dir];
			int nc = c + dc[dir];
			
			if (nr < 0 || nr >= N || nc < 0 || nc >= N || snailRoad[nr][nc] !=0) {
				dir = (dir+1)%4;
				nr = r+ dr[dir];
				nc = c+ dc[dir];
			}
			
			r = nr;
			c = nc;
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				sb.append(snailRoad[i][j]+" ");
				if (snailRoad[i][j] == findNum) {
					x = i+1;
					y= j+1;
				}
			}
			sb.append('\n');
		}
		System.out.print(sb.toString());
		System.out.println(x+" "+y);
	}

}
