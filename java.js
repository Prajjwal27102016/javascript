var dice;

var dices = ['dice-six-faces-one.png', 'dice-six-faces-two.png', 'dice-six-faces-three.png', 'dice-six-faces-four.png', 'dice-six-faces-five.png', 'dice-six-faces-six.png'];
var stopped = true;
var t;

function change() {
    var ramdom = maath.floor(Math.random() * 6);
    dice.innerHtml = dices[ramdom];
}

function stopstart() {
    if (stopped) {
        stopped = false;
        t = setInterval(change, 100);
    } else {
        clearInterval(t);
        stopped = true;
}
}

window.onload = function() {
    dice = document.getElementById('dice');
    stopstart();
}