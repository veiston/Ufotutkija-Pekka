// Add the spotlight element to your page
// <div id="spotlight" class="spotlight"></div>

// Add the script to your page
// <script src="/static/js/spotlight.js" defer></script>

// Add the styles to your page
// <link rel="stylesheet" href="/static/css/spotlight.css" />

const overlay = document.querySelector('#spotlight');

document.addEventListener('mousemove', (e) => {
    const x = e.clientX;
    const y = e.clientY;

    const gradient = `
		radial-gradient(
			circle 160px at ${x}px ${y}px,
			transparent 0%,
			rgba(0, 0, 0, 0.4) 40%,
			rgba(0, 0, 0, 0.6) 50%,
			rgba(0, 0, 0, 0.8) 70%,
			black 100%
		)
	`;

    overlay.style.maskImage = gradient;
    overlay.style.webkitMaskImage = gradient;
});