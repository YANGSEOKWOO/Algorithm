import java.util.*;

public class Main {
    static List<int[]> ladder = new ArrayList<>();
    static List<int[]> snake = new ArrayList<>();
    static boolean[] visited = new boolean[101];
    static int[] dp = new int[101];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // 사다리 수
        int m = sc.nextInt(); // 뱀 수

        for (int i = 0; i < n; i++) {
            ladder.add(new int[]{sc.nextInt(), sc.nextInt()});
        }

        for (int i = 0; i < m; i++) {
            snake.add(new int[]{sc.nextInt(), sc.nextInt()});
        }

        Arrays.fill(dp, Integer.MAX_VALUE);
        bfs();
        System.out.println(dp[100]);
    }

    static int isLadder(int number) {
        for (int[] l : ladder) {
            if (l[0] == number) {
                return l[1];
            }
        }
        return 0;
    }

    static int isSnake(int number) {
        for (int[] s : snake) {
            if (s[0] == number) {
                return s[1];
            }
        }
        return 0;
    }

    static void bfs() {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{1, 0}); // 위치, 이동 횟수
        visited[1] = true;
        dp[1] = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int cnt = current[1];

            for (int i = 1; i <= 6; i++) {
                int next = x + i;
                if (next <= 100 && !visited[next]) {
                    int ladderCheck = isLadder(next);
                    int snakeCheck = isSnake(next);

                    if (ladderCheck != 0) {
                        queue.add(new int[]{ladderCheck, cnt + 1});
                        visited[next] = true;
                        dp[next] = cnt + 1;
                    } else if (snakeCheck != 0) {
                        queue.add(new int[]{snakeCheck, cnt + 1});
                        visited[next] = true;
                        dp[next] = cnt + 1;
                    } else {
                        queue.add(new int[]{next, cnt + 1});
                        visited[next] = true;
                        dp[next] = cnt + 1;
                    }
                }
            }
        }
    }
}