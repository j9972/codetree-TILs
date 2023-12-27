import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args)throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String s=br.readLine();
        int result=0;

        for(int i=0; i<s.length(); i++){
            char start=s.charAt(i);
            for(int j=i+1; j<s.length(); j++){
                if(start=='(' && s.charAt(j)==')') result++;
            }
        }
        System.out.println(result);
    }
}