import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        sc.nextLine();

        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};

        int[][] arr = new int[n][m];
        int[][] distance = new int[n][m];
        boolean[][] visited = new boolean[n][m];

        for(int i=0; i<n; i++){
            String s = sc.nextLine();
            for(int j=0; j<m; j++){
                arr[i][j] = s.charAt(j) -'0';
            }
        }

        Queue<Node> q_now = new LinkedList<>();
        Queue<Node> q_next = new LinkedList<>();
        q_now.add(new Node(0,0));

        distance[0][0] = 0;
        visited[0][0] = true;

        while(!q_now.isEmpty()){
            Node node = q_now.poll();
            int x = node.x;
            int y = node.y;
            for(int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                if(nx>=0 && ny>=0 && nx<n && ny<m){
                    if(!visited[nx][ny]){
                        if(arr[nx][ny]==0){ // 벽이 없는 곳으로 이동 (벽을 부수지 않고 이동)
                            q_now.add(new Node(nx,ny));
                            visited[nx][ny] = true;
                            distance[nx][ny] = distance[x][y];
                        }else{ // 벽을 부수고 이동
                            q_next.add(new Node(nx,ny));
                            visited[nx][ny] = true;
                            distance[nx][ny] = distance[x][y]+1;
                        }
                    }
                }
            }
            if(q_now.isEmpty()){
                q_now = q_next;
                q_next = new LinkedList<>();
            }
        }


        System.out.println(distance[n-1][m-1]);

    }
}

class Node{
    int x,y;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
