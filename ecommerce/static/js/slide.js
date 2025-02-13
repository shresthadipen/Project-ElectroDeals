const brandsContainer = document.querySelector(".brands");
const brandSlides = document.querySelectorAll(".brand-container");

let counter = 0;
let totalSlides = brandSlides.length;

const updateSlides = () => {
    totalSlides = document.querySelectorAll(".brand-container").length; // Ensure correct count
};

const goNext = () => {
    updateSlides();
    if (counter < totalSlides - 1) {
        counter++;
        slideIndex();
    }
};

const goPrev = () => {
    updateSlides();
    if (counter > 0) {
        counter--;
        slideIndex();
    }
};

const slideIndex = () => {
    brandsContainer.style.transform = `translateY(-${counter * 100}%)`; 
};
