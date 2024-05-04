function highAndLow(numbers){

    //MI SOLUCION 1
    // var split = numbers.split(" ")

    // var splitit = split.map(e => {
    //     return parseInt(e)
    // })

    // var min = Math.min(...splitit)

    // var max = Math.max(...splitit)

    // var res = ""+max+" "+ min

    // return res

    //MI SOLUCION MEJORADA XD
    // var split = numbers.split(" ")

    // var min = Math.min(...split)

    // var max = Math.max(...split)

    // return `${max} ${min}`

    //SOLUCION DE OTRO XD, y MI SOLUCION MUCHO MAS MEJOR 
    split = numbers.split(' ')
    return `${Math.max(...split)} ${Math.min(...split)}`
}

console.log(highAndLow("1 2 3 4 5"));  // return "5 1"
console.log(highAndLow("1 2 -3 4 5")); // return "5 -3"
console.log(highAndLow("1 9 3 4 -5")); // return "9 -5"