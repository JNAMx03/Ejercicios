function maskify(cc) {
    // let ncc = ""
    // for (let i = 0; i < cc.length; i++) {
    //     if(i < cc.length-4){
    //         ncc += "#"
    //     }else{
    //         ncc += cc[i]
    //     }
    // }
    // return ncc
    
    console.log(cc);
    console.log(cc.replace(/.(?=.{4})/g, "#"));
    console.log(cc.replace(/.(?=....)/g, '#'));

}

console.log(maskify('4556364607935616'));
// console.log(maskify('1'));
// console.log(maskify('11111'));