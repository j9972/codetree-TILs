import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args)throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String s=br.readLine();
        int result=0;
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<s.length(); i++){
            char start=s.charAt(i);

            if(start=='('){
                stack.push(start);
            }
            if(!stack.isEmpty()){
                if(stack.peek()=='('){
                    int cnt=0;
                    for(int j=i+1; j<s.length(); j++){
                        char end=s.charAt(j);
                        if(end==')') cnt++;
                        if(j==s.length()-1) stack.pop();
                    }
                    result+=cnt;
                }
            }
        }
        System.out.println(result);
    }
}