import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;



public class a10_java_static_initializer_block 
{
    //Write your code here
    public static int B , H ;
    public static boolean flag = true;

    static
    {
        Scanner lc = new Scanner(System.in);
        B = lc.nextInt();
        H = lc.nextInt();

        if(B <= 0 || H <= 0)
        {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
            flag = false;
        }
        
        lc.close();

    }

    public static void main(String[] args){
  
        if(flag){
            int area=B*H;
            System.out.print(area);
        }

    }//end of main

}//end of class
