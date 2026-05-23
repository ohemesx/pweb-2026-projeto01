document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slide");
    const prevBtn = document.querySelector(".prev");
    const nextBtn = document.querySelector(".next");
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.remove("active");
            if (i === index) {
                slide.classList.add("active");
            }
        });
    }

    prevBtn.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    });

    nextBtn.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    });

    // inicia mostrando o primeiro slide
    showSlide(currentIndex);
});

window.onload = () => {
    const params = new URLSearchParams(window.location.search);
    if (params.get("animacao") === "1") {
        // morcego diagonal
        const bat1 = document.createElement("img");
        bat1.src = "/static/img/bat.png";
        bat1.classList.add("bat-diagonal");
        document.body.appendChild(bat1);


        // morcego direita → esquerda
        const bat3 = document.createElement("img");
        bat3.src = "/static/img/bat2.png";
        bat3.classList.add("bat-right-left");
        document.body.appendChild(bat3);

        // remove todos após animação
        [bat1, bat2, bat3].forEach(bat => {
            bat.addEventListener("animationend", () => bat.remove());
        });
    }
};



