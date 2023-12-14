import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
    이모티콘
 */
public class Main {
    static final int MAX =  2000;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt(); // 화면에 만들어야 될 이모티콘 개수
        int[][] dist = new int[MAX+1][MAX+1];
        Queue<Node> q = new LinkedList<>();

        for(int i=0; i<=MAX; i++){
            Arrays.fill(dist[i],-1);
        }
        Node start = new Node(1,0);
        q.add(start);
        dist[1][0] = 0;

        while(!q.isEmpty()){
            Node remove = q.remove();
            int x = remove.getScreen();
            int y = remove.getClip();

            if(dist[x][x]==-1){
                dist[x][x] = dist[x][y]+1;
                q.add(new Node(x,x));
            }

            if(y>0 && x+y<=MAX && dist[x+y][y]==-1){
                dist[x+y][y] = dist[x][y]+1;
                q.add(new Node(x+y,y));
            }

            if(x-1>=0 && dist[x-1][y]==-1){
                dist[x-1][y] = dist[x][y]+1;
                q.add(new Node(x-1,y));
            }

        }

        int ans = -1;
        for(int i=0; i<=s; i++){
            if(dist[s][i]!=-1){
                if(ans==-1 || ans>dist[s][i]){
                    ans = dist[s][i];
                }
            }
        }

        System.out.println(ans);

    }

}

class Node{
    private int screen;
    private int clip;

    public Node(int screen,int clip){
        this.screen = screen;
        this.clip = clip;
    }

    public int getScreen() {
        return screen;
    }

    public void setScreen(int screen) {
        this.screen = screen;
    }

    public int getClip() {
        return clip;
    }

    public void setClip(int clip) {
        this.clip = clip;
    }
}
