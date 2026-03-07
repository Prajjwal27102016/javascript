class Student {

    constructor(name) {

        this.studentName = name;

    }

    static hello() { // static method

        return "Hello!!";

    }

    static welcome(x) {

        return "Welcome " + x.studentName;

    }

    hi() {

        return "Hi " + this.studentName;

    }

}

myname = new Student("Carol");

console.log(Student.hello());

// Call 'hi()' on the 'myname' object:

console.log(myname.hi());

// Call 'welcome()' can access the object since parameter is passed

console.log(Student.welcome(myname));