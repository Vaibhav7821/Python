

class Demo {

	public static void main(String[] args) {
	
		int rows = 5;
		int num = 1;
		for(int i=1; i<=rows; i++){
		
			for(int j=1; j<=rows; ){
			
				int temp = num;
				int sum = 0;
				while(temp != 0){
					sum = sum+temp%10;
					temp = temp/10;
				}

				if(num % sum == 0){
					j++;
					System.out.print(num+"   ");

				}
				num++;


			}
			System.out.println();

		}
	}
}
