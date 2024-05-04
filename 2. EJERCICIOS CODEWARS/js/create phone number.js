function createPhoneNumber(numbers){
    var num = "(";

    numbers.forEach((e, i) => {
        num += e
        if(i === 2) num += ") "
        if(i === 5) num += "-"
    });

    return num
}

//solution 2
// function createPhoneNumber(numbers){
//     var format = "(xxx) xxx-xxxx";
    
//     for(var i = 0; i < numbers.length; i++)
//     {
//       format = format.replace('x', numbers[i]);
//     }
    
//     return format;
//   }

//solution 3
// function createPhoneNumber(numbers){
//     numbers = numbers.join('');
//     return '(' + numbers.substring(0, 3) + ') ' 
//         + numbers.substring(3, 6) 
//         + '-' 
//         + numbers.substring(6);
//   }

//solution 4
// function createPhoneNumber(numbers){
//     return numbers.join('').replace(/(...)(...)(.*)/, '($1) $2-$3');
// //  return numbers.join('').replace(/(\d{3})(\d{3})(\d{4})/,'($1) $2-$3');
//   }

console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));