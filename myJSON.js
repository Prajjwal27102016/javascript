var myObj = { name: "Prajjwal Singh Mandloi", age: 10, grade: 5 };
console.log(typeof (myObj))

var myJSON = JSON.stringify(myObj);
console.log(typeof (myJSON))

var newOBJ = JSON.parse(myJSON);

console.log(newOBJ)
console.log(typeof (newOBJ))