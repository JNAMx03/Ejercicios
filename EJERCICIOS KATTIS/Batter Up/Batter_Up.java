import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Batter_Up
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader lc = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        int n = Integer.parseInt(lc.readLine());
        String m = lc.readLine();
        String m_split[] = m.split(" ");
        for( int i = 0; i < m_split.length; i++)
        {
            sum = sum + Integer.parseInt(m_split[i]);
            if(m_split[i].equals("-1"))
            {
                n = n - 1;
                sum = sum + 1;
            }
        }
        System.out.println(sum/n);
    }
}