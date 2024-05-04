//SOLUCION MIA
// function addBinary(a,b) {
//     var c = a + b

//     return binary(c)
// }

// function binary(num){
//     return num ? binary(Math.floor(num/2)) + num%2 : ""
// }

//OTRA SOLUCION XD
function addBinary(a,b){
    return (a+b).toString(2)
}

console.log(addBinary(1,1));
console.log(addBinary(5,9));