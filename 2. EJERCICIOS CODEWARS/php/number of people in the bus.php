function number($bus_stops) {
    //MI FORMA :D
    $in = 0;
    for($i = 0, $i < count($bus_stops); $i++){
        $in = $in + $bus_stops[$i][0] - $bus_stops[$i][1];
    }
    return $in;

    //OTRA FORMA XD
    $in_bus = 0;
  
    foreach( $bus_stops as $bus_stop )
    {
        $in_bus +=  $bus_stop[0] - $bus_stop[1];
    } 
    
    return $in_bus;
}