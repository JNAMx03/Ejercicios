import java.io.*;
import java.util.*;
import java.text.DecimalFormat;
import java.text.Format;
import java.text.NumberFormat;

public class a13_java_currency_formatter {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        Locale indiaLocale = new Locale("en", "IN");
        NumberFormat d = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat i = NumberFormat.getCurrencyInstance(indiaLocale);
        NumberFormat c = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat f = NumberFormat.getCurrencyInstance(Locale.FRANCE);

        double payment = in.nextDouble();

        System.out.println("US: "     + d.format(payment));
        System.out.println("India: "  + i.format(payment));
        System.out.println("China: "  + c.format(payment));
        System.out.println("France: " + f.format(payment));


        in.close();
    }
    
}

//JAVA 8
