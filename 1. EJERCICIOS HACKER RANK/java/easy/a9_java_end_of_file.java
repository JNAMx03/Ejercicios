//https://www.hackerrank.com/challenges/java-end-of-file/problem?isFullScreen=true
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class a9_java_end_of_file {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner lc = new Scanner(System.in);
        //-----------------------------MIO LO ESTABA HACIENDO SUPER MAL
        /*String word = " ", txt = "";
        //boolean val = true;
        int i = 1;
        while(word.charAt(word.length()-1) != '.')
        {
            word = lc.next();
            char let = word.charAt(0);
            if(let == word.toUpperCase().charAt(0))
            {
                if(i == 1)
                {
                    String ii = Integer.toString(i);
                    txt = ii + " " + word;
                    i += 1;
                }
                else
                {
                    System.out.println(txt);
                    String ii = Integer.toString(i);
                    txt = ii + " " + word;
                    i += 1;
                }
                
            }
            else
            {
                if(word.charAt(word.length()-1) == '.')
                {
                    System.out.println(txt);
                    System.out.println(txt + " " + word);
                }
                else
                {
                    txt = txt + " " + word;
                }
                
            }
                
            
        }*/

        //--------------------ALGUIEN MAS
        int i = 0;
        while (lc.hasNextLine()) {
            System.out.println(++i + " " + lc.nextLine());
        }
        lc.close();
    }

    
}
