function solution(year) {
    if (year <= 100) {
        return 1
    } else if (year > 100  && year <= 999) {
        let a = year % 100;
        let b = Math.floor(year / 100);
        console.log(a);
        console.log(b);
        if (a !== 0) {
        return b + 1;
        }
        return b;
    } else if (year >= 1000 && year <= 2022) {
        let a = year % 100;
        let b = Math.floor(year / 100);
        if ((a !== 00)) {
        return b + 1;
        }
        return b;
    }
}
console.log(solution(0));
console.log(solution(200));
console.log(solution(1450));
console.log(solution(1700));
console.log(solution(2000));
