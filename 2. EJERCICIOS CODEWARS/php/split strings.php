function solution($str) {
    if(strlen($str) == 0)
    {
    return [];
  }
  else
    {
    $arr = str_split($str, 2);
    for ($x = 0; $x < strlen($str)/2; $x++)
    {
        if(strlen($arr[$x]) == 1 )
        {
          $arr[$x] = $arr[$x] . "_";
        }
    }
  
  return $arr;
  }

  /*una mejor manera
  if (empty($str))
    return [];
  if (strlen($str) % 2 != 0)
    $str .= "_";
  return str_split($str, 2);
  */
}