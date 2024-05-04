package QuaSel;

import java.io.*;

public class QS 
{
    public static void main(String[] args) throws IOException 
    {
        BufferedReader lc = new BufferedReader(new InputStreamReader(System.in));
        String a, b;
        int n1, n2;
        
        a = lc.readLine();
        n1 = Integer.parseInt(a);

        b = lc.readLine();
        n2 = Integer.parseInt(b);
        
        if(n1 > 0)
        {
            if(n2 > 0)
            {
                System.out.println("1");
            }
            else
            {
                System.out.println("4");
            }          
        }
        else
        {
            if(n2 > 0)
            {
                System.out.println("2");
            }
            else
            {
                System.out.println("3");
            }
        }      
    }  
}
