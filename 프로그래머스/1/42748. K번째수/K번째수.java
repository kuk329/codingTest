import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int n = commands.length;
        int[] answer = new int[n];
        int idx = 0;
        for(int[] command : commands){
            int[] tmp = Arrays.copyOfRange(array,command[0]-1,command[1]);
            Arrays.sort(tmp); // 오름차순 정렬
            answer[idx] = tmp[command[2]-1];
            idx++;
        }
        return answer;
    }
}