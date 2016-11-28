import java.util.Scanner;
import java.io.*;
/**
 * @author Richard Huang
 */
public class solution{
	public static void wrappingPaper() throws FileNotFoundException{
		try{
			Scanner sc=new Scanner(new File("data.txt"));
			int paper=0;
			while(sc.hasNext()){
				String s=sc.nextLine();
				int l=Integer.parseInt(s.substring(0,s.indexOf("x")));
				s=s.substring(s.indexOf("x")+1);
				int w=Integer.parseInt(s.substring(0,s.indexOf("x")));
				int h=Integer.parseInt(s.substring(s.indexOf("x")+1));
				int max=Math.max(Math.max(h,l),w);
				int min;
				if(max==l)
					min=h*w;
				else if(max==h)
					min=l*w;
				else
					min=l*h;
				paper+=2*(l*w+w*h+l*h)+min;
			}
			System.out.println(paper);
		}catch(FileNotFoundException error){
			System.out.println("File \"data.txt\" not found");
		}
	}
	public static void main(String args[]) throws FileNotFoundException{
		try{
			solution.wrappingPaper();
		}catch(FileNotFoundException error){
			System.out.println(error);
		}
	}
}
