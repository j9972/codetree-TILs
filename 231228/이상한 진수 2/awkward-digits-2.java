import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String strArr[]= s.split("");

        for(int i=0; i<strArr.length; i++){
            if(s.length()==1){
                if(strArr[i].equals("1")){
                    strArr[i]="0";
                    break;
                }else{
                    strArr[i]="1";
                    break;
                }
            }
            if(!strArr[i].equals("1")){
                strArr[i]="1";
                break;
            }
        }

        int z=1;
        int result=0;
        for(int i=strArr.length-1; i>=0; i--){
            result+=Integer.parseInt(strArr[i])*z;
            z*=2;
        }
        System.out.println(result);
    }
}