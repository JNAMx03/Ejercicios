function divisors($integer) {
    for ($i = 2; $i <= floor($integer / 2); $i++) {
        if ($integer % $i === 0) {
            $numbers[] = $i;
        }
    }
    return empty($numbers) ? $integer . ' is prime' : $numbers;
}