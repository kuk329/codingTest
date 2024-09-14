import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 4;
        char[][] a = new char[4][8];
        for(int i=0; i<n; i++){
            a[i]  = sc.next().toCharArray();
        }
        int k = sc.nextInt(); // 반복 횟수 입력받음

        while(k>0){
            k--;
            int no = sc.nextInt()-1; // 톱니바퀴 번호 입력
            int dir = sc.nextInt(); // 회전 방향 입력

            // 톱니바퀴들은 동시에 회전을 해야되기 때문에 각 톱니바퀴들의 회전 방향을 저장할 배열 선언
            int[] d = new int[n]; // 톱니바퀴 수 만큼 배열 생성
            d[no] = dir;

            // 왼쪽 톱니바퀴들 부터 확인
            for(int i=no-1; i>=0; i--){
                if(a[i][2]!=a[i+1][6]){
                    d[i] = -d[i+1];
                }else{
                    break;
                }
            }

            // 오른쪽 톱니바퀴들 확인
            for(int i=no+1; i<n; i++){
                if(a[i-1][2]!=a[i][6]){
                    d[i] = -d[i-1];
                }else{
                    break;
                }
            }

            // 저장한 회전 방향 정보들을 가지고 톱니바퀴를 회전시킴
            for(int i=0; i<n; i++){
                if(d[i]==0) continue;
                if(d[i]==1){
                    // 시계 방향 회전 (오른쪽으로 한칸씩 이동)
                    char temp = a[i][7];
                    for(int j=7; j>=1; j--){
                        a[i][j] = a[i][j-1];
                    }
                    a[i][0] = temp;

                }else if(d[i]==-1){
                    // 반시계 방향 회전 (왼쪽으로 한칸씩 이동)
                    char temp = a[i][0];
                    for(int j=0; j<7; j++){
                        a[i][j] = a[i][j+1];
                    }
                    a[i][7] = temp;
                }
            }
        }

        int ans = 0;
        if(a[0][0]=='1') ans+=1;
        if(a[1][0]=='1') ans+=2;
        if(a[2][0]=='1') ans+=4;
        if(a[3][0]=='1') ans+=8;

        System.out.println(ans);

    }
}
