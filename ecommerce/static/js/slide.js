const brandsContainer = document.querySelector(".brands");
const slides = document.querySelectorAll(".brand-container");
let counter = 0;
const slideHeight = slides[0].clientHeight;

const goNext = () => {
    if (counter < slides.length - 1) { 
        counter++;
        slideIndex();
    }
};

const goPrev = () => {
    if (counter > 0) { 
        counter--;
        slideIndex();
    }
};

const slideIndex = () => {
    brandsContainer.style.transform = `translateX(-${counter * slideHeight}px)`; 
};
