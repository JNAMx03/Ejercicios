// See https://aka.ms/new-console-template for more information

//convierte cada inicial de palabra en mayuscula

using System;
using System.Globalization;

string phrase = "How can mirrors be real if our eyes aren't real";

TextInfo ti = CultureInfo.CurrentCulture.TextInfo;

Console.WriteLine(ti.ToTitleCase(phrase));

