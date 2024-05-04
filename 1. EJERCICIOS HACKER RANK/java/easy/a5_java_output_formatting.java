//https://es.tutorialcup.com/java/string-format-java.htm

import java.util.*;

public class a5_java_output_formatting {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int i=0;i<3;i++){
            String s1=sc.next();
            int x=sc.nextInt();
            //Complete this line
            String n, m;
            if(x < 100)
            {
                //int aux = 15 - s1.length();
                n = String.format("%-15s", s1);
                m = String.format("%03d", x);
                System.out.println(n + m);
            }
            else
            {
                n = String.format("%-15s", s1);
                m = String.format("%d", x);
                System.out.println(n + m);
            }
        }
        System.out.println("================================");

        sc.close();

    }
    
}
