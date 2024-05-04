// See https://aka.ms/new-console-template for more information

// int num = 42145, aux = 0;

// int[] sNum = num.ToString().Select(o => Convert.ToInt32(o)-48).ToArray();

// foreach  (int c in sNum) { 
//     Console.WriteLine(c); 
// }

// for (int i = 0; i < sNum.Length-1; i++){
//     for (int j = i+1; j < sNum.Length; j++){
//         if(sNum[j] > sNum[i]){
//             aux = sNum[i];
//             sNum[i] =  sNum[j];
//             sNum[j] = aux;
//         }
//     }    
// }

// Console.WriteLine("-------------------------");

// foreach  (int c in sNum) { 
//     Console.WriteLine(c); 
// }

// Console.WriteLine("-------------------------");

// Console.WriteLine(sNum.Select((t, i) => t * Convert.ToInt32(Math.Pow(10, sNum.Length - i - 1)))
//     .Sum());


//----------------

// int num = 41245;

// Console.WriteLine(num.ToString().OrderByDescending(x => x));
// Console.WriteLine(string.Concat(num.ToString().OrderByDescending(x => x)));
// Console.WriteLine(int.Parse(string.Concat(num.ToString().OrderByDescending(x => x))));


//-------------

int num = 41245;

char[] arr = num.ToString().ToCharArray();
Array.Sort(arr);
Array.Reverse(arr);
Console.Write(Convert.ToInt32(new string(arr)));
