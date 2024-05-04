function square_digits($num){


    //OTRA SOLUCION NO SABES XD
    $numbers = str_split($num);
  
    foreach($numbers as &$number) {
        $number *= $number;
    }
    
    return implode('', $numbers);
}