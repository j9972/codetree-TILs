import java.util.*;
import java.io.*;

public class Main {
    public static int max = Integer.MIN_VALUE;
    public static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        int[][] arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - 2; j++) {
                for (int k = 0; k < N; k++) {
                    for (int l = 0; l < N - 2; l++) {
                        if ((i == k) && Math.abs(j - l) < 3) continue;

                        max = Math.max(max, (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[k][l] + arr[k][l + 1] + arr[k][l + 2]));

                    }
                }
            }
        }

        System.out.println(max);
    }
}