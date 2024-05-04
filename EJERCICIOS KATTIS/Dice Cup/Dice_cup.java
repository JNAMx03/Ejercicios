import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Dice_cup
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader lc = new BufferedReader(new InputStreamReader(System.in));
        String caras = lc.readLine();
        String caras_split[] = caras.split(" ");
        int /*a = Integer.parseInt(caras_split[0]),*/ x, menor, mayor;
        //int b = Integer.parseInt(caras_split[1]);
        if (Integer.parseInt(caras_split[0])/*a*/  <= /*b*/Integer.parseInt(caras_split[1]))
        {
            menor = Integer.parseInt(caras_split[0])/*a*/;
            mayor = Integer.parseInt(caras_split[1])/*b*/;
        }
        else
        {
            menor = Integer.parseInt(caras_split[1])/*b*/;
            mayor = Integer.parseInt(caras_split[0])/*a*/;
        }
        for(int i = 0; i <= mayor; i++)
        {
            x = 1 + i;
            if ((menor+1) == x)
            {
                System.out.println(x);
                menor = menor + 1 ;
            }
        }
    }
}