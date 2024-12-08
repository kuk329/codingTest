import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int A = sc.nextInt();
		int B = sc.nextInt();
		int result = 0;

		int[] arr1 = new int[A];
		int[] arr2 = new int[B];

		for (int i = 0; i < A; i++) {
			arr1[i] = sc.nextInt();
		}

		for (int i = 0; i < B; i++) {
			arr2[i] = sc.nextInt();
		}

		Arrays.sort(arr1);
		Arrays.sort(arr2);

		int a = A-1;
		int b = B-1;

		if (N % 2 == 1) { // 홀수
			// 2x1 타일 하나 선택
			result = arr1[a];
			a -= 1;
			N-=1;

		}
		while(N>0){
			int sum1 = 0;
			int sum2 = 0;
			if((a)>=0 && (a-1)>=0){
				sum1 = arr1[a] + arr1[a-1];
			}
			if(b>=0){
				sum2 = arr2[b];
			}
			if(sum1>sum2){
				result +=sum1;
				a-=2;
			}else{
				result+=sum2;
				b-=1;
			}
			N-=2;

		}
		System.out.println(result);
	}
}
