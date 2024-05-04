// See https://aka.ms/new-console-template for more information
static bool Solution(string str, string ending)
{
    // TODO: complete
    // if("(".Equals(")"))Console.WriteLine("si");
    // else Console.WriteLine("no");

    //MI SOLUCION, PURA POPO

    // char[] rstr = str.ToCharArray();
    // Array.Reverse(rstr);

    // char[] rending = ending.ToCharArray();
    // Array.Reverse(rending);

    // if(rending.Length > rstr.Length )return false;
    // if(rending.Length <= 0 || rstr.Length <= 0)return true;

    // for (int i = 0; i < rending.Length; i++)
    // {
    //     if(rending[i].Equals(rstr[i])){
    //        if(i == rending.Length-1){
    //         return true;
    //        }
    //     }
    // }
    // return false;

    //SOLUCION DE OTROS 1 XD

    //return str.EndsWith(ending);

    //SOLUCION DE OTROS 2 XD

    return (str.Length >= ending.Length) && str.Substring(str.Length - ending.Length).Equals(ending);
}

Console.WriteLine(Solution("abc", "bc")); // returns true
Console.WriteLine(Solution("abc", "d")); // returns false
Console.WriteLine(Solution("samurai", "ra")); // returns false
Console.WriteLine(Solution("abc", "abcd")); // returns false
Console.WriteLine(Solution("abc", "")); // returns true
Console.WriteLine(Solution(":-)",":-(")); // returns false
