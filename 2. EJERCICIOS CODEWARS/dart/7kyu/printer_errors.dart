//https://www.codewars.com/kata/56541980fa08ab47a0000040
//https://www.codewars.com/kata/56541980fa08ab47a0000040/solutions

import 'dart:io';

void main() {
  String? n = stdin.readLineSync();
  print(printerError("$n"));
}

String printerError(String s) {
  // SOLUTION 1
  final RegExp reError = new RegExp("[^a-m]");
  return "${reError.allMatches(s).length}/${s.length}";
  // SOLUTION 2
  //return RegExp(r"[nopqrstuvwxyz]").allMatches(s).length.toString() + "/" + s.length.toString();


}
