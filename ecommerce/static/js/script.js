
document.addEventListener("DOMContentLoaded", function() {
    const userIcon = document.getElementById("user-icon"); 
    const dropdown = document.querySelector(".dropdown"); 

    userIcon.addEventListener("click", function(event) {
        event.stopPropagation(); 
        dropdown.classList.toggle("show"); 
    });

    window.addEventListener("click", function(event) {
        if (!dropdown.contains(event.target)) {
            dropdown.classList.remove("show"); 
        }
    });
});
