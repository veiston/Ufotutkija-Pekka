document.addEventListener("DOMContentLoaded", () => {
    const flashlight = document.getElementById("flashlight");
    const audio = document.getElementById("flashlight-sound");
    const spotlight = document.getElementById('spotlight');

    let rotation = 0; // начальный угол
    flashlight.src = "/static/images/light.png";

    flashlight.addEventListener("click", () => {
        if (spotlight) {

            spotlight.classList.toggle('spotlight');

            if (spotlight.classList.contains('spotlight')) {
                     flashlight.style.transform = ``;
            } else {

                flashlight.style.transform = `scale(1, -1)`;
            }

            if (audio) {
                audio.currentTime = 0;
                audio.play();
            }
        }
    });
});