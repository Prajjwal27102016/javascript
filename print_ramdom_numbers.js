let count = 0;

while (count < 5) {
    let randomNumber = Math.floor(Math.random() * 100) + 1;
    console.log("Random Number " + (count + 1) + ": " + randomNumber);
    count++;
}