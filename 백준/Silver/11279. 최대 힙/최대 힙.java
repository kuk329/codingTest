import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> q= new PriorityQueue<>(Collections.reverseOrder());

        int x;

        for(int i = 0; i<n; i++){
            x = Integer.parseInt(br.readLine());
            if(x==0){
                Integer poll = q.poll();
                if(poll==null){
                    System.out.println(0);
                }else{
                    System.out.println(poll);
                }
            }else{
                q.add(x);
            }
        }

    }
}
