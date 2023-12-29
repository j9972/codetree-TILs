import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static int arr[];
    public static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            for (int j = i+2; j < N; j++) {
                if(Math.abs(i-j)>=2) {
                    int sum = arr[i] + arr[j];
                    max = Math.max(sum, max);
                }
            }
        }

        System.out.println(max);
    }
}