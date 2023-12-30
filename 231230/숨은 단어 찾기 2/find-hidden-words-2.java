import java.util.*;
import java.io.*;

public class Main {
    public static char map[][];
    public static int n, m;
    public static int result = 0;
    public static int[] dx = new int[]{1, 1, 1, -1, -1, -1, 0, 0};
    public static int[] dy = new int[]{-1, 0, 1, -1, 0, 1, -1, 1};

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new char[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = s.charAt(j);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'L') {
                    for (int k = 0; k < 8; k++) {
                        int cnt = 0;
                        int nx = i;
                        int ny = j;
                        for (int l = 0; l < 2; l++) {
                            nx += dx[k];
                            ny += dy[k];

                            if (nx < 0 || nx >= n || ny < 0 || ny >= m) break;
                            if (map[nx][ny] == 'E') cnt++;
                        }
                        if (cnt == 2) result++;
                    }
                }
            }
        }
        System.out.println(result);
    }
}