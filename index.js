document.addEventListener("DOMContentLoaded", function () {
    const carousels = document.querySelectorAll('.carousel');

    carousels.forEach(function (carousel) {
        const slides = carousel.querySelectorAll('.slide');
        let slideIndex = 0;

        showSlides();

        function showSlides() {
            slides.forEach(function (slide) {
                slide.style.display = "none";
            });

            slideIndex++;
            if (slideIndex > slides.length) {
                slideIndex = 1;
            }

            slides[slideIndex - 1].style.display = "block";

            setTimeout(showSlides, 2000); // Cambia cada 2 segundos
        }
    });
});

