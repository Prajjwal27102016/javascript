class Vehicle {
    constructor(brand, year) {
        this.brand = brand;
        this.year = year;
    }

    displayInfo() {
        console.log(`Brand: ${this.brand}`);
        console.log(`Year: ${this.year}`);
    }
}

class Car extends Vehicle {
    constructor(brand, year, model) {
        super(brand, year);
        this.model = model;
    }

    displayFullDetails() {
        this.displayInfo();
        console.log(`Model: ${this.model}`);
    }
}

const myCar = new Car("Tesla", 2026, "Model 3");
myCar.displayFullDetails();