import java.util.Scanner;

public class Main{

	static int recur(String s, int index, char last){
		if(s.length() == index){ // 문자열의 길이 까지만 반복
			return 1;
		}
		char start = (s.charAt(index)=='c'?'a':'0');
		char end = (s.charAt(index)=='c'?'z':'9');
		int ans = 0;
		for(char i=start; i<=end; i++){
			if(i!=last){
				ans += recur(s,index+1,i);
			}
		}
		return ans;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		System.out.println(recur(s,0,' '));
	}
}
