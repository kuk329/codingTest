import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] p = new int[n+1];
        int[] d = new int[1001];
        for(int i=1; i<=n; i++)
        {
            p[i] = sc.nextInt();
        }
   //     System.out.println(Arrays.toString(p));
        d[1] = p[1];

        for(int i=2; i<=n; i++){
            for(int j=0; j<=i; j++){
                d[i] = Math.max(d[i-j]+p[j],d[i]);
            }
        }

        System.out.println(d[n]);


    }
}
