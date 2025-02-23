function showSuggestions() {
    let input = document.getElementById("search-input").value;  
    let suggestionsBox = document.getElementById("suggestions-list");  

    if (input.length === 0) {
        suggestionsBox.style.display = "none"; 
        return;
    }

    fetch(`/search/?query=${input}`)
        .then(response => response.json())  
        .then(data => {
            suggestionsBox.innerHTML = "";  
            if (data.suggestions.length > 0) {
                data.suggestions.forEach(product => {
                    let item = document.createElement("div");
                    item.classList.add("suggestion-item");
                    item.innerHTML = `
                        <img src="${product.image}" alt="${product.name}">
                        <div class="suggestion-details">
                            <span class="suggestion-name">${product.name}</span>
                            <span class="suggestion-price">$${product.price}</span>
                        </div>
                    `;
                    suggestionsBox.appendChild(item);
                });
                suggestionsBox.style.display = "block"; 
            } else {
                suggestionsBox.style.display = "none";  
            }
        });
}