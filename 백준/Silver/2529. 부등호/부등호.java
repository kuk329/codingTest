import java.util.Scanner;

// 부등호
public class Main {

	static boolean permutation1(int[] arr) {
		int i = arr.length - 1;
		while (i > 0 && arr[i - 1] <= arr[i]) {
			i -= 1;
		}

		if (i <= 0) {
			return false;
		}

		int j = arr.length - 1;
		while (arr[j] >= arr[i - 1]) {
			j -= 1;
		}

		int temp = arr[i - 1];
		arr[i - 1] = arr[j];
		arr[j] = temp;

		j = arr.length - 1;
		while (i < j) {
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i += 1;
			j -= 1;
		}
		return true;

	}

	static boolean permutation2(int[] arr) {
		int i = arr.length - 1;
		while (i > 0 && arr[i - 1] >= arr[i]) {
			i -= 1;
		}

		if (i <= 0) {
			return false;
		}

		int j = arr.length - 1;
		while (arr[j] <= arr[i - 1]) {
			j -= 1;
		}

		int temp = arr[i - 1];
		arr[i - 1] = arr[j];
		arr[j] = temp;

		j = arr.length - 1;
		while (i < j) {
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i += 1;
			j -= 1;
		}
		return true;
	}

	static boolean check(int[] perm, char[] sign) {
		for (int i=0; i<sign.length; i++) {
			if (sign[i] == '<' && perm[i] > perm[i+1]) {
				return false;
			}
			if (sign[i] == '>' && perm[i] < perm[i+1]) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt();
		char[] arr = new char[k];
		for (int i = 0; i < k; i++) {
			arr[i] = sc.next().charAt(0);
		}

		int[] small = new int[k + 1];
		int[] big = new int[k + 1];
		for (int i = 0; i <= k; i++) {
			small[i] = i;
			big[i] = 9 - i;
		}

		// 최댓값
		do {
			if (check(big, arr)) {
				break;
			}
		} while (permutation1(big));

		// 최솟값
		do {
			if (check(small, arr)) {
				break;
			}
		} while (permutation2(small));


		for (int j : big) {
			System.out.print(j);
		}
		System.out.println();

		for (int j : small) {
			System.out.print(j);
		}

	}
}
