document.addEventListener("DOMContentLoaded", () => {
    const flashlight = document.getElementById("flashlight");
    const audio = document.getElementById("flashlight-sound");

    flashlight.addEventListener("click", (e) => {
        const spotlight = document.getElementById('spotlight');

        if (spotlight) {
            spotlight.classList.toggle('spotlight');

            if (audio) {
                audio.currentTime = 0;
                audio.play();
            }
        }
    });
});