import java.util.*;

public class Main {
    public static int n = 5;
    public static int[] arr = new int[]{1, 2, 3, 2, 6};

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int max=Integer.MIN_VALUE;

        for(int i=0; i<n; i++){
            int sum=0;
            arr[i]*=2;

            for(int j=0; j<n-1; j++){
                sum += Math.abs(arr[j]-arr[j+1]);
            }

            max=Math.max(sum,max);
            arr[i]/=2;
        }
        System.out.println(max);
    }
}