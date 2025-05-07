document.addEventListener("DOMContentLoaded", () => {
    const light = document.getElementById("light");
    const spotlight = document.getElementById('spotlight');

    const lightAudio = document.getElementById("light-sound");
    const lightIsBreakingAudio = document.getElementById("light-is-breaking-sound");
    const lightIsBrokenAudio = document.getElementById("light-is-broken-sound");

    const playLightSound = () => {
        if (lightAudio) {
            lightAudio.currentTime = 0;
            lightAudio.play();
        }
    }

    const playBreakingSound = async () => {
        if (lightIsBreakingAudio) {
            lightIsBreakingAudio.currentTime = 0;
            await lightIsBreakingAudio.play();
        }
    }

    const playBrokenSound = async () => {
        if (lightIsBrokenAudio) {
            lightIsBrokenAudio.currentTime = 0;
            await lightIsBrokenAudio.play();
        }
    }

    light.src = "/static/images/light.png";

    let isBroken = false;

    light.addEventListener("click", async () => {
        if (spotlight) {
            spotlight.classList.toggle('spotlight');
            light.classList.toggle('light--on');
            playLightSound();
            // if (!isBroken) {
            //     spotlight.classList.toggle('spotlight');
            //     light.classList.toggle('light--on');
            //     playLightSound();
            //
            //     const shouldBreak = Math.random() > 0.6 && !spotlight.classList.contains('spotlight');
            //
            //     if (shouldBreak) {
            //         await playBreakingSound();
            //
            //         setTimeout(async () => {
            //             await playBrokenSound();
            //             spotlight.classList.add('spotlight');
            //             light.classList.add('light--opacity-2');
            //         }, 2000);
            //
            //         isBroken = true;
            //     }
            // } else {
            //     light.classList.toggle('light--on');
            //     playLightSound();
            // }
        }
    });
});