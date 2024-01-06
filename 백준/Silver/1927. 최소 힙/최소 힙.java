import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
//        Scanner sc =new Scanner(System.in);
//        int n = sc.nextInt();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 우선순위 큐(힙)
        PriorityQueue<Integer> queue = new PriorityQueue<>();

        int x;
        for(int i=0; i<n; i++ ){
           // int x = sc.nextInt();
             x = Integer.parseInt(br.readLine());
            if(x==0){
                Integer poll = queue.poll(); // 우선순위가 가장 높은 값 제거(비었을때는 null 리턴)
                if(poll==null){
                    System.out.println(0);
                }else{
                    System.out.println(poll);
                }

            }else{
                queue.add(x);
            }

        }




    }
}
