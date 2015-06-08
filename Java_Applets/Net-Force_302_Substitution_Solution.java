import java.util.Scanner;

public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("==========================");
    System.out.println("Net-Force Solution: 204");
    System.out.println("--By Pranshu");
    System.out.println("==========================");
    Scanner s = new Scanner(System.in);
    System.out.println("\nTry a password: ");
    String str1;
    str1 = s.nextLine();
 
    int i = 0;
    for (int j = 0; j < str1.length(); j++)
    {
        i += str1.charAt(j);
        System.out.println(i);
    }
    
    if(i==448){
    	System.out.println("You have solved the challenge!");   }
    else {
    	System.out.println("Nope. Try another."); }
 }
}