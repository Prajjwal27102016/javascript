window.onload = function () {

    let seconds = 0;

    let milliseconds = 0;

    const appendMilliseconds = document.getElementById("milliseconds");

    const appendSeconds = document.getElementById("seconds");

    const buttonStart = document.getElementById("start");

    const buttonStop = document.getElementById("stop");

    const buttonReset = document.getElementById("reset");

    let interval;

    buttonStart.onclick = function () {

        clearInterval(interval);

        interval = setInterval(startTimer, 10);

    };

    buttonStop.onclick = function () {

        clearInterval(interval);

    };

    buttonReset.onclick = function () {

        clearInterval(interval);

        seconds = 0;

        milliseconds = 0;

        appendMilliseconds.innerHTML = "00";

        appendSeconds.innerHTML = "00";

    };

    function startTimer() {

        milliseconds++;

        if (milliseconds < 10) {

            appendMilliseconds.innerHTML = "0" + milliseconds;

        } else {

            appendMilliseconds.innerHTML = milliseconds;

        }

        if (milliseconds >= 100) {

            seconds++;

            milliseconds = 0;

            appendMilliseconds.innerHTML = "00";

            appendSeconds.innerHTML = seconds < 10 ? "0" + seconds : seconds;

        }

    }

};