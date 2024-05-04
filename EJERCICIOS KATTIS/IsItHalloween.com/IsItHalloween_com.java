import java.io.*;

public class IsItHalloween_com
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader lc = new BufferedReader (new InputStreamReader(System.in));
        String date = lc.readLine().toUpperCase();
        String date_split[] = date.split(" ");
        if(date_split[0].equals("OCT") || date_split[0].equals("DEC"))
        {
            if(date_split[1].equals("31") || date_split[1].equals("25"))
            {
                System.out.println("yup");
            }
            else
            {
                System.out.println("nope");
            }
        }
        else
        {
            System.out.println("nope");
        }
    }
}