import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static int map[][];
    public static int cnt = 0;
    public static boolean visited[][];
    public static int result[][];
    public static int[] dx = new int[]{1, 1, 1, -1, -1, -1, 0, 0};
    public static int[] dy = new int[]{-1, 0, 1, -1, 0, 1, -1, 1};

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        map = new int[20][20];
        visited = new boolean[20][20];

        for (int i = 1; i <= 19; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= 19; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int black = 1, white = 2;
        for (int i = 1; i <= 19; i++) {
            for (int j = 1; j <= 19; j++) {
                if (map[i][j] == black && !visited[i][j]) {
                    cnt = 0;
                    result = new int[10][2];
                    dfs(i, j, black,0);
                } else if (map[i][j] == white && !visited[i][j]) {
                    cnt = 0;
                    result = new int[10][2];
                    dfs(i, j, white,0);
                }
            }
        }

        if (cnt<5) {
            System.out.println(0);
        }

    }

    public static void dfs(int x, int y, int color,int idx) {
        visited[x][y] = true;
        result[idx][0] = x;
        result[idx][1] = y;
        cnt++;

        if (cnt == 5 ) {
            System.out.println(color);
            System.out.printf("%d %d", result[2][0], result[2][1]);
            return;
        }
        for (int i = 0; i < 8; i++) {
            int cx = x + dx[i];
            int cy = y + dy[i];

            if (cx >= 1 && cy >= 1 && cx < 20 && cy < 20) {
                if (!visited[cx][cy] && map[cx][cy] == color) {
                    dfs(cx, cy, color,idx+1);
                }
            }
        }
    }
}