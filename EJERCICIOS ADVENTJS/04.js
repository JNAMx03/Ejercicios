function createXmasTree(height) {
    // ¡Y no olvides también poner los turrones!
    //var limit = height + (height-1)

    var tree = ""
    var y = height
    
    for (let i = 1; i <= height; i++) {
        var a = "";
        let x = i + (i-1)
        for (let j = 1; j <= x; j++) {
            a += "*"
        }

        var g = "";
        for (let k = (y-1); k > 0; k--) {
            g += "_";
            
        }
        y--

        tree += g + a + g + "\n"
        
    }


    var gt = ""
    for (let k = (height-1); k > 0; k--) {
        gt += "_";
    }
    var t = gt + "#" + gt

    tree += t + "\n" + t

    return tree
}

console.log(createXmasTree(5));