document.getElementById("submitBtn").addEventListener("click", verify);

function verify() {
    var x = document.getElementById("pwd").value;
    document.getElementById("txt").innerHTML = "";

    if (document.getElementById("pwd").value !== document.getElementById("confirm").value) {
        document.getElementById("txt").innerHTML += "Password and confirm password must be the same<br>";
    }
    
    if (x.length < 8) {
        document.getElementById("txt").innerHTML += "Password must be greater than 8 characters";
    }
}
