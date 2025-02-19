document.addEventListener('click', function(event) {
    if (event.target.classList.contains('update-cart')) {
        const productId = event.target.dataset.product; 
        const action = event.target.dataset.action;
        console.log('Product ID:', productId, 'Action:', action);

        if (user === "AnonymousUser") {
            console.log('Not Logged in');
        } else {
            updateUserOrder(productId, action);
        }
    }
});


function updateUserOrder(productId, action) {
    console.log('Sending data...');

    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data);
        location.reload()
    })
}

function getToken(name) {
    let cookieValue = null;
    if (document.cookie) {
        document.cookie.split(";").forEach(cookie => {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.split("=")[1]);
            }
        });
    }
    return cookieValue;
}


const csrftoken = getToken("csrftoken");

function getCookie(name) {
    var cookieArr = document.cookie.split(";");

    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        if(name == cookiePair[0].trim()) {

            return decodeURIComponent(cookiePair[1]);
        }
    }

    return null;
}
var cart = JSON.parse(getCookie('cart'))