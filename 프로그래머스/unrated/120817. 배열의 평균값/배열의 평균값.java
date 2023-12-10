import java.util.*;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int sum = Arrays.stream(numbers).sum();
        double len = numbers.length;
        answer = sum/len;
        return answer;
      
    }
}