function showModal(options) {
  let modal = document.getElementById("modalBox");
  let msg = document.getElementById("modalBoxMessage");
  let btns = document.getElementById("modalBoxButtons");
  msg.innerHTML = options.message;
  btns.innerHTML = "";
  let result = null;
  options.buttons.forEach(function (btnOpt) {
    let btn = document.createElement("button");
    btn.textContent = btnOpt.label;
    btn.className = btnOpt.className || "button";
    btn.onclick = function () {
      result = btnOpt.value;
      modal.style.display = "none";
      if (typeof options.onClose === "function") {
        options.onClose(result);
      }
    };
    btns.appendChild(btn);
  });
  modal.style.display = "flex";
}
window.showModal = showModal;

// setTimeout(function () {
/*    showModal({
        message: "This flight costs $100. Do you want to proceed?",
        buttons: [
          { label: "Yes", value: true },
          { label: "No", value: false },
        ],
        onClose: function (confirmed) {
          if (confirmed) {
            handleAirportClick(code);
          } else {
            map.removeLayer(flightLine);
          }
        },
      });
    }, 500); */

// showInfoModal("Your message to the user here");
