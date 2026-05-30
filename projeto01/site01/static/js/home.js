window.onload = () => {
    const vanContainer = document.querySelector(".van-container"); 

    const leftLight = document.createElement("div");
    leftLight.classList.add("headlight", "left");

    const rightLight = document.createElement("div");
    rightLight.classList.add("headlight", "right");

    vanContainer.appendChild(leftLight);
    vanContainer.appendChild(rightLight);
};
