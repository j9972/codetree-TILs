import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static String S;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        S = br.readLine();

        int result=0;
        for(int i=0; i<S.length(); i++) {
            if(S.charAt(i)=='C'){
                for(int j=i+1; j<S.length(); j++){
                    if(S.charAt(j)=='O'){
                        for(int k=j+1; k<S.length(); k++){
                            if(S.charAt(k)=='W'){
                                result++;
                            }
                        }
                    }
                }
            }

        }
        System.out.println(result);
    }
}