function solution(inputString) {
    let a= Math.floor(inputString.length/2)
    for (let i = 0; i < a; i++) {
        if(inputString[i] !== inputString[inputString.length-i-1]){
            return false
        }
    }
    return true
}

console.log(solution('aabaa'));
console.log(solution('aaajhlñ'));