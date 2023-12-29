import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static int[][] arr;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N][2];
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int cnt = 1;
        while (cnt < N-1) {
            int distance = 0;
            for (int i = 0; i < N-1; i++) {
                int x2 =i+1;
                if (cnt == i) continue;
                if (cnt == x2) x2++;
                distance += Math.abs(arr[i][0] - arr[x2][0]) + Math.abs(arr[i][1] - arr[x2][1]);
            }
            cnt++;
            if (min > distance) min = distance;
        }
        System.out.println(min);
    }
}