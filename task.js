function divisible_5(num) {
    if (num % 5 === 0) {
        return num + ' is divisible with 5';
    } else {
        return num + ' is not divisible with 5';
    }
}

console.log(divisible_5(10));
console.log(divisible_5(12)); 