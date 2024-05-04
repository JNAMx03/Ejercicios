
var maximumWealth = function(accounts) {
    let mayor = 0
    for(let i=0; i < accounts.length;i++){
        console.log(accounts[i]);
        let suma=0
        for(let j=0; j<accounts[i].length; j++){
            suma+=accounts[i][j]
    }
    if(suma>mayor)mayor=suma
    
 }
 console.log(mayor); 
};


const accounts = [[2,8,7],[7,1,3],[1,9,5]]

maximumWealth(accounts)
