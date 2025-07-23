function showTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    var session = "AM";

    if (hours === 0) {
        hours = 12;
    }

    if (hours > 12) {
        hours -= 12;
        session = "PM";
    }

    h = (h<10) ? "0" + h : h;
    m = (m<10) ? "0" + m : m;
    s = (s<10) ? "0" + s : s;

    var time = hours + ":" + minutes + ":" + seconds + " " + session;
    document.getElementById("myclockdisplay").innerText = time;
    setTimeout(showTime, 1000);
}

showTime();