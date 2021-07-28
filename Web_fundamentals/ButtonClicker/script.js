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

function likes(element) {
    alert("Ninja was Liked!");
}