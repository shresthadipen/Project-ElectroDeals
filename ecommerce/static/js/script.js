// Wait for the document to be fully loaded before running the script
document.addEventListener("DOMContentLoaded", function() {
    const userIcon = document.getElementById("user-icon"); // User icon element
    const dropdown = document.querySelector(".dropdown"); // The dropdown container

    // Toggle the 'show' class on the dropdown when user clicks on the user icon
    userIcon.addEventListener("click", function(event) {
        event.stopPropagation(); // Prevent click from propagating to the window
        dropdown.classList.toggle("show"); // Toggle the 'show' class to display the dropdown
    });

    // Close the dropdown if the user clicks outside of it
    window.addEventListener("click", function(event) {
        if (!dropdown.contains(event.target)) {
            dropdown.classList.remove("show"); // Hide the dropdown if the click is outside
        }
    });
});
