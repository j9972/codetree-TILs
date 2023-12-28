import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static int map[][];
    public static int max=Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        StringTokenizer st;
        map = new int[n][n];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++){
                map[i][j]=Integer.parseInt(st.nextToken());
            }
        } 
        maxCnt();
    }

    public static void maxCnt(){   
        for(int i=0; i<n; i++){
            for(int j=0; j<n-2; j++){
                int cnt = map[i][j] + map[i][j+1] + map[i][j+2];
                max=Math.max(max,cnt);
            }
        }
        System.out.println(max);
    }
}