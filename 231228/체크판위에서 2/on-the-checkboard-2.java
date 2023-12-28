import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        char map[][] = new char[R][C];
        int cnt=0;

        for(int i=0; i<R; i++){
            String s = br.readLine();
            for(int j=0; j<C; j++){
                map[i][j]=s.charAt(j);
            }
        } 

        for(int i=1; i<R; i++){
            for(int j=1; j<C; j++){
                for(int k=i+1; k<R-1; k++){
                    for(int l=j+1; l<C-1; l++){
                        if(map[0][0]!= map[i][j] &&
                        map[i][j]!= map[k][l] &&
                        map[k][l]!= map[R-1][C-1])
                        cnt++;
                    }
                }
            }
        }
        System.out.println(cnt);
    }
}