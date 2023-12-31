import java.util.Scanner;

public class Main {
    private static final long MOD = 1_000_000_000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        long[][] d = new long[n+1][10];

        for (int i = 1; i <= 9; i++) {
            d[1][i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= 9; j++) {
                if (j == 0) {
                    d[i][j] = d[i - 1][j + 1];
                } else if (j == 9) {
                    d[i][j] = d[i - 1][j - 1];
                } else {
                    d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1];
                }
                d[i][j] = d[i][j] % MOD;
            }
        }

        long result = 0;
        for(int k=0; k<=9; k++){
            result+=d[n][k];
        }
        System.out.println(result%MOD);


    }
}
