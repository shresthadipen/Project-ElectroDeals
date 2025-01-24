const slides = document.querySelectorAll(".brand-container");
let counter = 0;

slides.forEach((slide, index) => {
    slide.style.left = `${index * 100}%`; 
});

const goNext = () => {
    if(counter < slides.length){
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
    slides.forEach((slide) => {
        slide.style.transform = `translateX(-${counter * 103}%)`; 
    });
};
