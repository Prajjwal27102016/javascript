var date = new Date()
console.log(date)

date.getDate()
console.log("Today's date: " + date.getDate())

date.getHours()
console.log("Current hour: " + date.getHours())

date.getMinutes()
console.log("Current minutes: " + date.getMinutes())


date.getSeconds()
console.log("Current seconds: " + date.getSeconds())

date.getMilliseconds()
console.log("Current milliseconds: " + date.getMilliseconds())

var day;

switch (new Date().getDay()) {

    case 0:

        day = "Sunday";

        break;

    case 1:

        day = "Monday";

        break;

    case 2:

        day = "Tuesday";

        break;

    case 3:

        day = "Wednesday";

        break;

    case 4:

        day = "Thursday";

        break;

    case 5:

        day = "Friday";

        break;

    case 6:

        day = "Saturday";

}

console.log("Today is: " + day)