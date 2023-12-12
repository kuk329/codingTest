import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * 숨바꼭질 4 - 13913
 */
public class Main {

    private static final int MAX = 200000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        boolean[] check = new boolean[MAX+1];
        int[] dist = new int[MAX+1];
        int[] from = new int[MAX+1];
        check[n] = true;
        dist[n] = 0;
        from[n] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(n);

        while (!q.isEmpty()) {
            int now = q.poll();

            if(now==k)
                break;

            int next = now + 1;
            if (next <= MAX && check[next] == false) {
                q.add(next);
                dist[next] = dist[now] + 1;
                from[next] = now;
                check[next] = true;
            }
            next = now - 1;
            if (next >= 0 && check[next] == false) {
                q.add(next);
                dist[next] = dist[now] + 1;
                from[next] = now;
                check[next] = true;
            }

            next = now * 2;
            if (next <= MAX && check[next] == false) {
                q.add(next);
                dist[next] = dist[now] + 1;
                from[next] = now;
                check[next] = true;
            }
        }

        System.out.println(dist[k]);

        go(from,n,k);

    }

    public static void go(int[] position,int n, int k){
        if(n!=k){
            go(position,n ,position[k]);
        }
        System.out.print(k +" ");

    }
}
