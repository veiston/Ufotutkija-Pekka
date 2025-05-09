const fadeAudio = document.querySelector("#fadeAudio");
fadeAudio.volume = 0;
fadeAudio.muted = false;

const fadeInAudio = (audioElement, targetVolume = 1, duration = 8000) => {
  if (!audioElement) return;

  audioElement.volume = 0;
  const step = 0.01;
  const intervalTime = (duration * step) / targetVolume;

  const fadeInterval = setInterval(() => {
    if (audioElement.volume < targetVolume) {
      audioElement.volume = Math.min(audioElement.volume + step, targetVolume);
    } else {
      clearInterval(fadeInterval);
    }
  }, intervalTime);
};

fadeInAudio(fadeAudio);
