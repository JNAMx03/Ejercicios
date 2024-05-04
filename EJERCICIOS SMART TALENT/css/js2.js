input = "3\nNoah,blue\nEuge,red\nKi Na Ma,red"

a = input.split("\n")
console.log(a);

a.forEach(e => {
    b = e.split(",")
    if(b[0].toLowerCase().includes("n") && b[0].toLowerCase().includes("a")){
        if(b[1] == "red"){
            console.log(b[0]);
        }
    }
    
});