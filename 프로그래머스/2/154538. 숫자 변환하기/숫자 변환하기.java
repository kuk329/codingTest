import java.util.*;

class Solution {
    static int MAX_NUM = 1000000;
    boolean[] visited = new boolean[MAX_NUM+1];
    int[] distance = new int[MAX_NUM+1];
    Queue<Integer> tree = new LinkedList<Integer>();
    
    public int solution(int x, int y, int n) {
        Arrays.fill(distance,-1);
        tree.offer(x); // 큐
        visited[x] = true; // 방문 처리
        distance[x] = 0;
        
        while(!tree.isEmpty()){
            int k = tree.poll();
            if(k==y) return distance[k];
            
            int tmp = k + n;
            if(tmp<=MAX_NUM && !visited[tmp]){
                visited[tmp] = true;
                distance[tmp] = distance[k] + 1;
                tree.offer(tmp);
            }
            tmp = k*2;
            if(tmp<=MAX_NUM && !visited[tmp]){
                visited[tmp] = true;
                distance[tmp] = distance[k] + 1;
                tree.offer(tmp);
            }
            tmp = k*3;
            if(tmp<=MAX_NUM && !visited[tmp]){
                visited[tmp] = true;
                distance[tmp] = distance[k] + 1;
                tree.offer(tmp);
            }
            
            
        }
        
        return distance[y];
    }
}