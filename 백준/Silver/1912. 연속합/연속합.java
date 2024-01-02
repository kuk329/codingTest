import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        int[] a = new int[n];
        int[] d = new int[n];

        for(int i=0; i<n; i++){
            a[i] = sc.nextInt();
        }

        d[0] = a[0];

        for(int i=1; i<n; i++){
            d[i] = a[i];
            d[i] = Math.max(d[i],d[i-1]+a[i]);
        }


        int result = d[0];
        for(int i=1; i<n; i++){
            result = Math.max(result,d[i]);
            }

        System.out.println(result);

        }



}
