function toggleLogin(element) {
    if (element.innerText === "Login") {
        element.innerText = "Logout";
    } else {
        element.innerText = "Login";
    }

}

function removeDefinition(element) {
    element.remove();
}


let count = 3;
function handleLike(element) {
    count++;
    document.getElementById("likeCount").innerText = count;
    
    
    element.style.color = "red";
    element.style.backgroundColor = "blue";
}


function handle13Likes(element) {
    alert("The '13 likes' button was clicked!");
    element.style.padding = "20px";
}


function handle37Likes(element) {
    alert("The '37 likes' button was clicked!");
    element.style.borderColor = "red";
    element.style.borderWidth = "5px";
}