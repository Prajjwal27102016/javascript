name = "Prajjwal"
console.log(name[7])
name.toUpperCase()
console.log(name.toUpperCase())
name.toLowerCase()
console.log(name.toLowerCase())
name.startsWith("P")
console.log(name.startsWith("P"))
name.startsWith("p")
console.log(name.startsWith("p"))
name.endsWith("l")
console.log(name.endsWith("l"))
name.endsWith("L")
console.log(name.endsWith("L"))
Math.round(Math.random() * 10000000000000000)
console.log(Math.round(Math.random() * 10000000000000000))

var fruits = ["Apple", "Mango", "Grapes", "Watermelon", "Jack Fruit", "Banana"];
var text = "";
var i;

for (i = 0; i < fruits.length; i++) {
    text += fruits[i] + "\n";
}
console.log(text)