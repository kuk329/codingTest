import java.util.*;
public class Main {

    static ArrayList<Integer>[] a; // 간선을9 저장할 리스트
    static boolean[] c; // 방문 여부를 저장할 배열

    public static void dfs(int x) {

        c[x] = true; // 해당 정점 방문 처리
        System.out.printf(x + " ");
        for (int y : a[x]) {
            if (c[y] == false) { // 아직 해당 정점을 방문하지 않았으면
                dfs(y);
            }
        }
    }

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(start); // 처음 방문한 정점을 큐에 삽입
        c[start] = true; // 해당 정점 방문처리
        while(!q.isEmpty()){
            int x= q.remove(); // index가 0 인 객체 삭제
            System.out.printf(x+" ");
            for(int y:a[x]){
                if(c[y]==false){
                    c[y]=true; // 방문처리
                    q.add(y); // 큐에 삽입
                }
            }
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 정점 번호
        int m = sc.nextInt(); // 간선 개수
        int start = sc.nextInt(); // 시작 번호
        a = new ArrayList[n + 1]; // 간선 정보를 저장.
        for (int i = 0; i <=n; i++) {
            a[i] = new ArrayList<Integer>(); // arraylist 배열에 arrayList를 저장.
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            a[u].add(v);
            a[v].add(u);
        }

        for (int i = 0; i <= n; i++) {
            Collections.sort(a[i]); // 간선을 오름차순 정렬
        }

        c = new boolean[n + 1];
        dfs(start);
        System.out.println();
        c = new boolean[n+1]; // 다시 초기화 (false)
        bfs(start);
        System.out.println();
    }
}
