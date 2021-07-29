var cPic = document.querySelector("#ProfilePic");

console.log(cPic);

function change(element) {
    cPic.src = "./imgs/tom.jpg";
}

function cUp() {
    var likes = parseInt(document.getElementById('lcount').value, 10);
    likes = isNaN(likes) ? 0 : likes;
    likes++;
    document.getElementById('lcount').value = likes + " " + 'like(s)';
}

function cUp2() {
    var likes = parseInt(document.getElementById('lcount2').value, 10);
    likes = isNaN(likes) ? 0 : likes;
    likes++;
    document.getElementById('lcount2').value = likes + " " + 'like(s)';
}

function cUp3() {
    var likes = parseInt(document.getElementById('lcount3').value, 10);
    likes = isNaN(likes) ? 0 : likes;
    likes++;
    document.getElementById('lcount3').value = likes + " " + 'like(s)';
}