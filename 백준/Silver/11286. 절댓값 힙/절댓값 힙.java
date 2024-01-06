import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>((a,b)->{
            int abs1 = Math.abs(a);
            int abs2 = Math.abs(b);

            if(abs1==abs2) return a>b? 1:-1; 
            return abs1-abs2;

        });


        for (int i = 0; i < n; i++) {
            x = sc.nextInt();
            if (x == 0) {
                Integer out = queue.poll();
                if(out==null){
                    System.out.println(0);
                }else{
                    System.out.println(out);
                }

            } else {
                queue.add(x);
            }
        }

    }
}
