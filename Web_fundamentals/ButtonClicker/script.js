function turnOff(element) {
    if (element.innerText == "Login") {
        element.innerText = "LogOut";
    } else {
        element.innerText = "Login";
    }
}

function add(element) {
    element.remove();
}


var count = 0;
var countElement = document.querySelector("#LC");

function likes() {
    count++;
    countElement.innerText = count + " " + 'Like(s)'
    alert("Ninja was liked");
}


var count2 = 0;
var CE2 = document.querySelector("#LC2");

function inc() {
    count2++;
    CE2.innerText = count2 + " " + 'Like(s)'
}