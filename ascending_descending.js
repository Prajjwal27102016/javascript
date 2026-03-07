array1 = [1, 2, 5, 5, 6, 8, 9, 23, 45];
array1.reverse();
console.log("reversed array: " + array1);
array1.sort(function(a, b) {return a - b;});
console.log("ascending order: " + array1);
array1.sort(function(a, b) {return b - a;});
console.log("descending order: " + array1);