let slideIndex = 0;                                      // номер текущего слайда
const slides = document.querySelectorAll('.slides img'); // все картинки слайдера

function showSlide(index) {
    slides.forEach((img, i) => {
        img.classList.toggle('active', i === index); // active только у нужной картинки
    });
}

function nextSlide() {
    slideIndex = (slideIndex + 1) % slides.length; // % — зацикливание: после последнего идёт первый
    showSlide(slideIndex);
}

function prevSlide() {
    slideIndex = (slideIndex - 1 + slides.length) % slides.length; // назад с зацикливанием
    showSlide(slideIndex);
}

setInterval(nextSlide, 3000); // автопрокрутка каждые 3 секунды