document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".alert-cart").forEach(function (btn) {
        btn.addEventListener("click", function () {
            var userChoice = confirm("You need to log in to add items to the cart. Do you want to log in now?");
            
            if (!userChoice) {
                event.preventDefault(); 
            }else{
                window.location.href = "/login/"
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".alert-buy").forEach(function (btn) {
        btn.addEventListener("click", function () {
            var userChoice = confirm("You need to log in buy the item. Do you want to log in now?");
            
            if (!userChoice) {
                event.preventDefault(); 
            }else{
                window.location.href = "/login/"
            }
        });
    });
});
