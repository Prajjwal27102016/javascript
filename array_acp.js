const student = {
    name: "Alex",
    course: "Computer Science",
    level: "Intermediate"
};

const subjects = ["Math", "Physics", "Coding", "Design"];

console.log(student.name);
console.log(student.course);

console.log(subjects[0]);
console.log(subjects[2]);

subjects.pop();
const displayArray = subjects.join(", ");

console.log(displayArray);