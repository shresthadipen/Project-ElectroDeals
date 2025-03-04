document.addEventListener("DOMContentLoaded", function() {
    // sidebar click
    const dashboardLink = document.getElementById("dashboard-link");
    const usersLink = document.getElementById("users-link");
    const ordersLink = document.getElementById("orders-link");
    const messagesLink = document.getElementById("messages-link");
    const productsLink = document.getElementById("products-link");
    const brandsLink = document.getElementById("brands-link");
    const categoriesLink = document.getElementById("categories-link");
    const settingsLink = document.getElementById("settings-link");

    // display content of sidebar
    const dashboardContent = document.getElementById("dashboard-content");
    const usersContent = document.getElementById("users-content");
    const ordersContent = document.getElementById("orders-content");
    const messagesContent = document.getElementById("messages-content");
    const productsContent = document.getElementById("products-content");
    const brandsContent = document.getElementById("brands-content");
    const categoriesContent = document.getElementById("categories-content");
    const settingsContent = document.getElementById("settings-content");

    function hideAllContent() {
        dashboardContent.style.display = "none";
        usersContent.style.display = "none";
        ordersContent.style.display = "none";
        messagesContent.style.display = "none";
        productsContent.style.display = "none";
        brandsContent.style.display = "none";
        categoriesContent.style.display = "none";
        settingsContent.style.display = "none";
    }

    dashboardLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        dashboardContent.style.display = "block";
    });

    usersLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        usersContent.style.display = "block";
    });

    ordersLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        ordersContent.style.display = "block";
    });

    messagesLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        messagesContent.style.display = "block";
    });

    productsLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        productsContent.style.display = "block";
    });

    brandsLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        brandsContent.style.display = "block";
    });

    categoriesLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        categoriesContent.style.display = "block";
    });

    settingsLink.addEventListener("click", function(event) {
        event.preventDefault();
        hideAllContent();
        settingsContent.style.display = "block";
    });
});
