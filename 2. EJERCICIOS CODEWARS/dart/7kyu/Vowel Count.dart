import 'dart:io';

void main() {
  String? n = stdin.readLineSync();
  print(getCount("$n"));
}

//int getCount(String inputStr) {
  //your code here
  //SOLUTION 1
  // print(inputStr);
  // var count = 0;
  // var vowels = <String>["a", "e", "i", "o", "u"];
  // for (int i = 0; i < inputStr.length; i++) {
  //   if (vowels.contains(inputStr[i])) count++;
  // }
  // return count;

  //SOLUTION 2
  //return inputStr.split('').fold(0, (a, b) => a += 'aeiou'.contains(b) ? 1 : 0 );
//}

//SOLUTION 3
int getCount(String str) => new RegExp('[aeiou]').allMatches(str).length;
