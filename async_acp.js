async function startProject() {
    const result = await new Promise((resolve) => {
        setTimeout(() => {
            resolve("data received successfully!");
        }, 2000);
    });

    console.log(result);
    console.log("project task completed.");
}

startProject();

console.log("project is starting......");
console.log(":)")