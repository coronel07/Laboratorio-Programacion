
    let slideIndex = 0;
    showSlides();

    function showSlides() {
        let slides = document.getElementsByClassName("slide");
        let captions = document.getElementsByClassName("caption");

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
            captions[i].style.display = "none";
        }

        slideIndex++;
        if (slideIndex > slides.length) { slideIndex = 1 }

        slides[slideIndex - 1].style.display = "block";
        captions[slideIndex - 1].style.display = "block";

        setTimeout(showSlides, 2000); // Cambia cada 2 segundos
    }

