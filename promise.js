function delayedPrint() {

    return new Promise((resolve) => {

        setTimeout(() => {

            for (let i = 1; i <= 10; i++) {

                console.log(i);

            }

            resolve("Finished printing after 5 sec");

        }, 5000);

    });

}

console.log("hello world");

delayedPrint().then((message) => {

    console.log(message);

});

console.log(":)")