import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * 숨바꼭질 3
 */
public class Main {
    private static final int MAX = 200000;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        Queue<Integer> q_now = new LinkedList<>();
        Queue<Integer> q_next = new LinkedList<>();

        boolean[] visited = new boolean[MAX+1]; // 방문 여부
        int[] distance = new int[MAX+1];// 거리 저장

        distance[n] =0;
        q_now.add(n);
        visited[n] = true;

        while(!q_now.isEmpty()){
            int now = q_now.remove();

            if(now*2<=MAX && visited[now*2]==false){
                q_now.add(now*2);
                visited[now*2] = true;
                distance[now*2] = distance[now];
            }

            if(now-1>=0 && visited[now-1]==false){
                q_next.add(now-1);
                visited[now-1] = true;
                distance[now-1] = distance[now]+1;
            }
            if(now+1<=MAX && visited[now+1]==false){
                q_next.add(now+1);
                visited[now+1] = true;
                distance[now+1] = distance[now]+1;
            }
            if(q_now.isEmpty()){
                q_now= q_next;
                q_next = new LinkedList<>();
            }
        }

        System.out.println(distance[k]);


    }
}
