import java.util.*;
import java.io.*;

public class Main {
    public static String s;
    public static int max = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine();

       for(int i=0; i<s.length(); i++){
            findBinaryMax(i);
       }
        System.out.println(max);
    }
    public static void findBinaryMax(int n){
        int sum=0;
        int p=0;

        for(int i=s.length()-1; i>=0; i--){
            if(i==n){
                sum+=(((s.charAt(i)-'0')+1)%2)*Math.pow(2,p);
            }else{
                sum+=(s.charAt(i)-'0')*Math.pow(2,p);
            }
            p++;
            if(sum>max) max=sum;
        }
    }
}