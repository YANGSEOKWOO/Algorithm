import java.util.*;

public class Main {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int n, m;
    static char[][] graph;
    static boolean[][] visited;
    static int[][] rock;

    static class Node {
        int x, y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static void bfs(int a, int b) {
        Deque<Node> deque = new LinkedList<>();
        deque.add(new Node(a, b));
        visited[a][b] = true;
        rock[a][b] = 0;

        while (!deque.isEmpty()) {
            Node current = deque.poll();
            int x = current.x;
            int y = current.y;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny]) {
                    if (graph[nx][ny] == '1') { // 벽
                        rock[nx][ny] = Math.min(rock[nx][ny], rock[x][y] + 1);
                        deque.addLast(new Node(nx, ny));
                    } else { // 빈칸
                        rock[nx][ny] = Math.min(rock[nx][ny], rock[x][y]);
                        deque.addFirst(new Node(nx, ny));
                    }
                    visited[nx][ny] = true;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        m = sc.nextInt(); // 열
        n = sc.nextInt(); // 행
        sc.nextLine(); // 개행 처리

        graph = new char[n][m];
        visited = new boolean[n][m];
        rock = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            graph[i] = line.toCharArray();
            Arrays.fill(rock[i], (int) 1e9);
        }

        bfs(0, 0);
        System.out.println(rock[n - 1][m - 1]);
    }
}