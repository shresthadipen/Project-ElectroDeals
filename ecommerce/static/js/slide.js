let currentIndex = 0;

    // Get the brands container and its children
    const brandsContainer = document.querySelector('.brands');
    const totalBrands = document.querySelectorAll('.brand-container').length;

    // Function to move the slider
    function moveSlider(direction) {
        // Update the current index based on the direction of the click
        currentIndex += direction;

        // Prevent the index from going out of bounds
        if (currentIndex < 0) {
            currentIndex = 0;
        } else if (currentIndex >= totalBrands) {  // Adjust this number based on how many brands to show at once
            currentIndex = totalBrands;
        }

        // Move the brands container based on the index
        brandsContainer.style.transform = `translateX(-${currentIndex * 220}px)`; // 220px is the width of each brand
    }