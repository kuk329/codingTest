import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 징검다리 건너기
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        long[] stones = new long[N+1]; // index : 1 ~ N
        long[] dp = new long[N+1]; // 각 돌까지 건널때 필요한 최소 힘

        for(int i=1; i<=N; i++){
            stones[i] = Long.parseLong(st.nextToken());

        }
        for(int j=2; j<=N; j++){
            long minValue = Long.MAX_VALUE;

            for(int i=1; i<j; i++){
                long temp = (j-i)*(1+Math.abs(stones[i]-stones[j]));
                if(minValue > Math.max(dp[i],temp)){
                    minValue = Math.max(dp[i],temp);
                }
            }
            dp[j] = minValue;
        }

        System.out.println(dp[N]);

    }
}
