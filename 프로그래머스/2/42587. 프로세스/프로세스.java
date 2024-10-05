import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        // 우선순위 큐 선언
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        
        // 우선순위 큐에 데이터 삽입
        for(int i=0; i<priorities.length; i++){ 
            queue.offer(priorities[i]);
        }
        
        while(!queue.isEmpty()){
            for(int i=0; i<priorities.length; i++){
                if(queue.peek() == priorities[i]){
                    queue.poll();
                    answer++;
                    
                    if(i == location){
                        return answer;
                    }
                }
            }
        }
        
        
        
        
        return answer;
    }
}