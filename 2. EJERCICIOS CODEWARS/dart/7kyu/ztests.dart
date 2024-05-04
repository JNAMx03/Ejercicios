import 'dart:io';

void main() {
  //String? n = stdin.readLineSync();
  String x = "aaaabbbbjjjjhhh";
  final RegExp reError = new RegExp("[^a-m]");
  
  print({reError.allMatches(x).length});
}
