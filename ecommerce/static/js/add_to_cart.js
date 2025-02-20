const addToCartButtons = document.querySelectorAll(".update-cart");

addToCartButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const productId = this.dataset.product;
    const action = this.dataset.action;

    console.log("Product ID:", productId, "Action:", action);

    if (typeof user === "undefined") {
      console.error("User variable is not defined.");
      return;
    }

    console.log("User:", user);

    if (user === "AnonymousUser") {
      console.log("Not Logged in");
    } else {
      console.log("Sending data");
      updateUserOrder(productId, action);
    }
  });
});

function updateUserOrder(productId, action) {
  console.log("Sending data...");

  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productId: productId,
      action: action,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Response:", data);
      location.reload();
    });
}

function getToken(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    document.cookie.split(";").forEach((cookie) => {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.split("=")[1]);
      }
    });
  }
  return cookieValue;
}

const csrftoken = getToken("csrftoken");

