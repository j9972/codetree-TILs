import java.util.*;
import java.io.*;

public class Main {


    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String strArr[] = s.split("");
        int result = 0;

        for (int i = 0; i < s.length() - 3; i++) {
            for (int j = i + 1; j < s.length() - 2; j++) {
                String start = strArr[i] + strArr[j];
                if (start.equals("((")) {
                    String end = s.substring(j+1,s.length());
                    if(end.contains("))")){
                        result++;
                        break;
                    }
                }
            }
        }
        System.out.println(result);

    }
}