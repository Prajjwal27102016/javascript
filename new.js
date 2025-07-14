var choice = promt("welcome to area calculator.\n please enter your choice:\n1. area of rectangle\n2. area of triangle\n3. area of circle\n4. pallercome");

if (choice == 1) {
    var l = prompt("enter the length");
    var b = prompt("enter the breadth");
    var result = number(1)*number(b)
    alert("the area is " + result)
}
if (choice == 2) {
    var h = prompt("enter the height")
    var b = prompt("enter the base")
    var result = number(h) * number(b) /2
    alert("the area is " + result)
}
if (choice == 3) {
    var r = prompt("enter the radius")
    var result = 3.14 * number(r) * number(r)
    alert("the area is " + result)
}
if (choice == 4) {
    var l = prompt("enter the height")
    var b = prompt("enter the corresponding base")
    var result = (number(h) + number(cb))
    alert("the area is " + result)
}

    