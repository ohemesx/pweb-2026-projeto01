window.onload = () => {
    const vanContainer = document.querySelector(".van-container"); 

    // cria os faróis
    const leftLight = document.createElement("div");
    leftLight.classList.add("headlight", "left");

    const rightLight = document.createElement("div");
    rightLight.classList.add("headlight", "right");

    // adiciona à página
    vanContainer.appendChild(leftLight);
    vanContainer.appendChild(rightLight);
};
