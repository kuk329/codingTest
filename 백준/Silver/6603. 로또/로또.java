import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer> lotto = new ArrayList<>(); // 정답을 담을 전역 변수
    static int len;

    private static void bt(int[] arr,int idx, int cnt){
        if(cnt==6) {
            for(int num : lotto){
                System.out.print(num+ " "); // 6개 다 선택되면 바로 출력
            }
            System.out.println();
            return; // 더이상 진행 X
        }

        if(idx==len) return; // 마지막 index에 있는 번호까지 확인을 했을 경우 더이상 진행 X

        lotto.add(arr[idx]); // 선택한 로또 번호 추가
        bt(arr,idx+1,cnt+1);
        lotto.remove(lotto.size()-1);
        bt(arr,idx+1,cnt);


    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true){
            int k = sc.nextInt();
            if(k==0) break; // Test case 종료 조건
            int[] arr = new int[k];

            for(int i = 0; i<k; i++){
                arr[i] = sc.nextInt();
            }
            len = arr.length;
            bt(arr,0,0);
            System.out.println();
        }



    }
}
