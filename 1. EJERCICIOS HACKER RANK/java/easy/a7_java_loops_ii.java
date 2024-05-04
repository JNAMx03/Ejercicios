import java.util.*;
import java.util.concurrent.ForkJoinPool;
import java.io.*;

public class a7_java_loops_ii {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            for (int j = 0; j < n; j++) {
                a =  a + ((int)Math.pow(2, j) * b);
                System.out.print(a + " ");
                System.out.print((j==n-1)?"\n":"");
            }
        }

        

        in.close();
    }
    
}
