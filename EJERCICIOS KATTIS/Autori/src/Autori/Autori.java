package Autori;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Autori 
{
    public static void main(String[] args) throws IOException 
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a,A,b;
        String c = "";
        
        a = br.readLine();
        A = a.toUpperCase();
        
        String z[] = A.split("-");
        
        for (String item : z) {
            //System.out.println(item);
            c += item.charAt(0);      
        }
        System.out.println(c);
    }
}
