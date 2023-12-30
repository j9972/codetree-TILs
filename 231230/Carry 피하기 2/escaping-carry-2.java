import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static int arr[];
    public static int max = -1;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    boolean carry = false;

                    if (arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10) carry = true;
                    if (arr[i] % 100 / 10 + arr[j] % 100 / 10 + arr[k] % 100 / 10 >= 10) carry = true;
                    if (arr[i] % 1000 / 100 + arr[j] % 1000 / 100 + arr[k] % 1000 / 100 >= 10) carry = true;
                    if (arr[i] % 10000 / 1000 + arr[j] % 10000 / 1000 + arr[k] % 10000 / 1000 >= 10) carry = true;
                    if (!carry) max = Math.max(max, arr[i] + arr[j] + arr[k]);
                }
            }
        }
        System.out.println(max);
    }
}