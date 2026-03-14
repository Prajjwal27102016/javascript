function delayedPrint(callback) {

    setTimeout(() => {

        for (let i = 1; i <= 10; i++) {

            console.log(i);

        }

        callback("Finished printing after 5 sec");

    }, 5000);

}

console.log("hello world");

delayedPrint((message) => {

    console.log(message);

});

console.log("Hello world for the 2nd time")