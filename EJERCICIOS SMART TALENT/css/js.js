input = "5,10,15/2,4,6"

a = input.split("/")

b = a[0].split(",")

c = a[1].split(",")

for (let i = 0; i < b.length; i++) {
    b[i] = Number(b[i]) + Number(c[i])
    
}
console.log(b);