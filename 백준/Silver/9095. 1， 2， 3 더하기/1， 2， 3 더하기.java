import java.util.Scanner;

/**
 *  1,2,3 더하기 (9095번)
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // 반복할 횟수 입력

        for(int k=0; k<t; k++){
            int n = sc.nextInt(); // 정수 입력
            int[] d = new int[11];
            d[1] = 1;
            d[2] = 2;
            d[3] = 4;
            for(int i=4; i<=n; i++){
                d[i] = d[i-1] + d[i-2] + d[i-3];
            }
            System.out.println(d[n]);
        }
    }
}
