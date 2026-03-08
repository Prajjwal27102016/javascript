function printSeries() {
    let a = 0, b = 1, count = 0;
    while (count < 10) {
        console.log(a);
        let temp = a;
        a = b;
        b = temp + b;
        count++;
    }
}
console.log(printSeries());
