import java.util.*;
import java.security.*;

public class a11_java_int_to_string {
    public static void main(String[] args) {

        Scanner lc = new Scanner(System.in);

        int n = lc.nextInt();
        String s = Integer.toString(n);

        if(n == Integer.parseInt(s))
        {
            System.out.println("Good job");
        }
        else
        {
            System.out.println("Wrong answer");
        }

        lc.close();
    }

}
