document.addEventListener("DOMContentLoaded", () => {
  const airportButton = document.getElementById("airportButton");
  const shopButton = document.getElementById("shopButton");

  airportButton.addEventListener("click", () => {
    window.location.href = "/travel";
  });

  shopButton.addEventListener("click", () => {
    window.location.href = "/shop";
  });
});


