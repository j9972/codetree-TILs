import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static int[] arr;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N];
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N; i++) {
            int sum = 0;
            for (int j = 0; j < N; j++) {
                int dist = (j + N - i) % N;
                sum += dist * arr[j];
            }
            min = Math.min(sum, min);
        }
        System.out.println(min);
    }
}