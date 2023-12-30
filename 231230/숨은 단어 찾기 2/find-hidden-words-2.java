import java.util.*;
import java.io.*;

public class Main {
    public static String map[][];
    public static int n, m;
    public static int cnt = 0;
    public static boolean visited[][];
    public static int[] dx = new int[]{1, 1, 1, -1, -1, -1, 0, 0};
    public static int[] dy = new int[]{-1, 0, 1, -1, 0, 1, -1, 1};

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new String[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            String strArr[] = s.split("");
            for (int j = 0; j < m; j++) {
                map[i][j] = strArr[j];
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j].equals("L")) {
                    dfs(i, j, 1);
                }
            }
        }
        System.out.println(cnt);
    }

    public static void dfs(int x, int y, int idx) {
        visited[x][y] = true;

        if (idx >= 3) {
            cnt++;
        }
        for (int i = 0; i < 8; i++) {
            int cx = x + dx[i];
            int cy = y + dy[i];

            if (cx >= 0 && cy >= 0 && cx < n && cy < m) {
                if (!visited[cx][cy] && map[cx][cy].equals("E")) {
                    dfs(cx, cy, idx + 1);
                }
            }
        }
    }
}