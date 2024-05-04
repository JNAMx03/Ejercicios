package alphabet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
//import java.util.Iterator;
import java.util.Map;

public class NewAlphabet 
{
    public static void main(String[] args) throws IOException 
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, String> map = new HashMap<String, String>();
        map.put("A", "@");        map.put("B", "8");        map.put("C", "(");
        map.put("D", "|)");        map.put("E", "3");        map.put("F", "#");
        map.put("G", "6");        map.put("H", "[-]");        map.put("I", "|");
        map.put("J", "_|");        map.put("K", "|<");        map.put("L", "1");
        map.put("M", "[]\\/[]");        map.put("N", "[]\\[]");        map.put("O", "0");
        map.put("P", "|D");        map.put("Q", "(,)");        map.put("R", "|Z");
        map.put("S", "$");        map.put("T", "']['");        map.put("U", "|_|");
        map.put("V", "\\/");        map.put("W", "\\/\\/");        map.put("X", "}{");
        map.put("Y", "`/");        map.put("Z", "2");
        
        char cadenaOR[];
        cadenaOR = br.readLine().toUpperCase().toCharArray();
        //String cadenaMIN = cadenaOR.toLowerCase();
        String key = "";
        
        for (char item : cadenaOR ) 
        {
            String calve = String.valueOf(item);
            if(map.containsKey(calve))
            {
                key += map.get(calve);
            }else{
                key += item;
            }        
        }
        System.out.println(key);
    }  
}
