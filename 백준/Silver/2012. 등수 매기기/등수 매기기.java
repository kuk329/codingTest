import java.util.Arrays;
import java.util.Scanner;

// 등수 매기기
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] scores = new int[n];
		long result = 0;
		
		for(int i=0; i<n; i++){
			scores[i] = sc.nextInt();
		}
		
		Arrays.sort(scores); // 배열 오름차순 정렬
		
		
		for(int i=0; i<n; i++){
			result += Math.abs(scores[i]-(i+1));
		}

		System.out.println(result);
		
		
	}
}
