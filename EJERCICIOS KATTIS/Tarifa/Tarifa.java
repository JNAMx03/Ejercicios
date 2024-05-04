import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Tarifa
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader lc = new BufferedReader(new InputStreamReader(System.in));
        String xx, nn, pp;
        int x, n, p, a, b = 0;
        xx = lc.readLine();
        x = Integer.parseInt(xx);
        nn = lc.readLine();
        n = Integer.parseInt(nn);
        for(int i = 0; i < n; i++)
        {
            pp = lc.readLine();
            p = Integer.parseInt(pp);
            a = x-p;
            b = b + a;
        }
        System.out.print(b+x);
    }
}