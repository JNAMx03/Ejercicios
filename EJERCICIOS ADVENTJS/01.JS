function contarOvejas(ovejas) {
    // aquí tu magia
    const arr = []
    ovejas.forEach((v) => {
      if(v.color === "rojo" && v.name.toLowerCase().includes("n") && v.name.toLowerCase().includes("a")){
        arr.push(v)
      }
    })
    return arr;
  }

  const ovejas = [
    { name: 'Noa', color: 'azul' },
    { name: 'Euge', color: 'rojo' },
    { name: 'Navidad', color: 'rojo' },
    { name: 'Ki Na Ma', color: 'rojo'},
    { name: 'AAAAAaaaaa', color: 'rojo' },
    { name: 'Nnnnnnnn', color: 'rojo'}
  ]

  console.log(contarOvejas(ovejas));