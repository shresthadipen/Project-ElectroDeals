document.addEventListener("DOMContentLoaded", function () {
    var addToCartBtn = document.querySelector(".alert-cart");

    if (addToCartBtn) {
        addToCartBtn.addEventListener("click", function () {
            var userChoice = confirm("You need to log in to add items to the cart. Do you want to log in now?");
            
            if (userChoice) {
                window.location.href = "/login/";  
            } 
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    var addToCartBtn = document.querySelector(".alert-buy");

    if (addToCartBtn) {
        addToCartBtn.addEventListener("click", function () {
            var userChoice = confirm("You need to log in to buy items. Do you want to log in now?");
            
            if (userChoice) {
                window.location.href = "/login/";  
            } 
        });
    }
});