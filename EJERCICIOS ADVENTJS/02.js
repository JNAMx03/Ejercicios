const carta = "bici coche balón _playstation bici coche peluche";

function listGifts(letter) {
  var obj = {}
  var arr = letter.split(" ")
  arr.forEach(e =>{
    if(e[0] !== "_" && isNaN(e)){
        if(!obj.hasOwnProperty(e) ){
            obj[e] = arr.filter(c => c === e).length
        }
    }
  })
  return obj;
}

const regalos = listGifts(carta)

console.log(regalos)
