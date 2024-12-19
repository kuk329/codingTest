import java.util.Scanner;

// 십자카드 문제
public class Main {

	private static boolean checkClockNum(String str){ // 해당 숫자가 시계수인지 판별하는 함수
		StringBuilder tmp = new StringBuilder();
		int min_num = 9999;

		for(int i=0; i<4; i++){
			tmp.append(str.charAt(i));
			tmp.append(str.charAt((i+1)%4));
			tmp.append(str.charAt((i+2)%4));
			tmp.append(str.charAt((i+3)%4));


			if(Integer.parseInt(String.valueOf(tmp))<min_num){
				min_num = Integer.parseInt(String.valueOf(tmp));
			}

			tmp = new StringBuilder();

		}

		if(min_num == Integer.parseInt(str)){
			return true;
		}

			return false;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] nums = new int[4];

		for (int i = 0; i < 4; i++) {
			nums[i] = sc.nextInt();
		}

		int min_num = 9999;
		int num = 0;
		int count = 0;

		StringBuilder tmp = new StringBuilder();

		for (int i = 0; i < 4; i++) {
			tmp.append(nums[i]);
			tmp.append(nums[(i + 1) % 4]);
			tmp.append(nums[(i + 2) % 4]);
			tmp.append(nums[(i + 3) % 4]);

			num = Integer.parseInt(tmp.toString());
			if (min_num > num) {
				min_num = num;
			}
			tmp = new StringBuilder();
		}
		
		for(int i=1111; i<min_num; i++){
			if(String.valueOf(i).contains("0") || !checkClockNum(String.valueOf(i)))
				continue;

			count+=1;
		}
		System.out.println(count+1);
	}


}