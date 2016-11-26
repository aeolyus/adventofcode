import java.util.Scanner;
import java.io.*;
/**
 * @author Richard Huang
 */
public class solution{
	static int floor=0;
	public static void findFloor() throws FileNotFoundException{
		try{
			Scanner sc=new Scanner(new File("data.txt"));
			String s=sc.next();
			for(int i=0;i<s.length();i++){
				if(s.charAt(i)=='(')
					floor++;
				else
					floor--;
			}
			System.out.println(floor);
		}catch(FileNotFoundException error){
			System.out.println("File \"data.txt\" not found");
		}
	}
	public static void findPosition(int j) throws FileNotFoundException{
		floor=0;
		try{
			Scanner sc=new Scanner(new File("data.txt"));
			String s=sc.next();
			for(int i=floor;i<s.length();i++){
				if(s.charAt(i)=='(')
					floor++;
				else
					floor--;
				if(floor==j){
					System.out.println(i+1);
					break;
				}
			}
		}catch(FileNotFoundException error){
			System.out.println("File \"data.txt\" not found");
		}
	}
	public static void main(String args[]) throws FileNotFoundException{
		try{
			solution.findFloor();
			solution.findPosition(-1);
		}catch(FileNotFoundException error){
			System.out.println(error);
		}
	}
}
