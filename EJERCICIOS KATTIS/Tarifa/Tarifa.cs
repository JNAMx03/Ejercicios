using System;
namespace ejercicios_kattis
{
    class Tarifa
    {
        static void Main(string[] args)
        {
            int x, n, p, a, b = 0, i;
            x = Convert.ToInt32(Console.ReadLine());
            n = Convert.ToInt32(Console.ReadLine());
            for (i = 0; i < n; i++)
            {
                p = Convert.ToInt32(Console.ReadLine());
                a = x - p;
                b = b + a; 
            }
            Console.WriteLine (b+x);
        }
    }
}
