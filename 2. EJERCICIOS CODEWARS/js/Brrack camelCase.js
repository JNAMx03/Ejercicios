function solution(string) {
    //MI SOLUCION XD
    // var xd = []
    // var inicio = 0, final = 0
    // for (let i = 0; i < string.length; i++) {
    //     if(string[i] === string[i].toUpperCase()){
    //         final = i
    //         xd.push(string.substring(inicio, final))
    //         inicio = i
    //         console.log(i);
    //     }        
    // }
    // xd.push(string.substring(inicio))
    // return xd.join(" ")

    //OTRA SOLUCION
    return(string.replace(/([A-Z])/g, ' $1'));
}

console.log(solution('camelCasing'));
console.log(solution('camelCasingTest'));