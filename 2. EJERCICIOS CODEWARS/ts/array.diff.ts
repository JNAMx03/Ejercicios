export function arrayDiff(a: number[], b: number[]): number[] {
    const diff = []
    for (let i = 0; i < a.length; i++) {
        if(!b.includes(a[i]))
        {
            diff.push(a[i])
        }
        
    }
    return  diff;

    //MEJOR SOLUCION
    //return a.filter(e => !b.includes(e));
}
  

arrayDiff([], [4, 5])
arrayDiff([3, 4], [3])
arrayDiff([1, 8, 2], [])
arrayDiff([1, 2, 3], [1, 2])