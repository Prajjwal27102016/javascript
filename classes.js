class Student {

    constructor(name, year) {

        this.name = name;

        this.year = year;

    }

    // Age method

    age() {

        let date = new Date();

        return date.getFullYear() - this.year;

    }

}

// Using the class with two objects

const student26 = new Student("Prajjwal Singh Mandloi", 2016);

console.log("My name is " + student26.name + ". I was born in " + student26.year + ". And my age is " + student26.age());

const student14 = new Student("Harshil Dewarsher", 2016);

console.log("My name is " + student14.name + ". I was born in " + student14.year + ". And my age is " + student14.age());