function isValid(letter) {
    // ¡No dejes que el Grinch gane!
    var a = letter.indexOf("(")
    var b = letter.indexOf(")")

    console.log(a);
    console.log(b);

    if(a >= 0 && b >= 0 && b > a+1){
        var c = letter.slice(a, b+1)
        
    }else{
        return false
    }

    for (let i = 1; i < c.length-1; i++) {
        if(c[i] === "[" || c[i] === "{" || c[i] === "]" || c[i] === "}" || c[i] ==="(" || c[i] ===")"){
            return false
        }
    }
    return true

    //console.log(c);

    
}

const carta1 = "bici coche (balón) bici coche peluche" // -> ✅
const carta2 = "(muñeca) consola bici" // ✅

const carta3 = "bici coche (balón bici coche" // -> ❌
const carta4 = "peluche (bici [coche) bici coche balón" // -> ❌
const carta5 = "(peluche {) bici" // -> ❌
const carta6 = "() bici" // ❌
const carta7 = "(()) bici" // ❌

console.log(isValid(carta1));
console.log(isValid(carta2));
console.log(isValid(carta3));
console.log(isValid(carta4));
console.log(isValid(carta5));
console.log(isValid(carta6));
console.log(isValid(carta7));