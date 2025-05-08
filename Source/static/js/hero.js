document.addEventListener("DOMContentLoaded", () => {
  const startButton = document.getElementById("startButton");
  const nameForm = document.getElementById("nameForm");
  const continueWelcomeButton = document.getElementById("continueWelcomeButton");
  const indexScreen = document.getElementById("indexScreen");
  const nameEntryScreen = document.getElementById("nameEntryScreen");
  const welcomeScreen = document.getElementById("welcomeScreen");
  const playerNameInput = document.getElementById("playerName");
  const welcomeText = document.getElementById("welcomeText");

  let messages = [];
  let currentMessageIndex = 0;
  let playerName = "";

  const buttonLabels = {
    1: "Open",
    2: "Hurry up",
    3: "Go ahead"
  };

  const updateContinueButtonText = () => {
    continueWelcomeButton.textContent = buttonLabels[currentMessageIndex] || "Continue";
  };

  const createPlayer = async (name) => {
    try {
      const response = await fetch("/player/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name })
      });
      return await response.json();
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const initWelcomeScreen = () => {
    messages = [
      `Hello, ${playerName}, our best UFO hunter!\nYou've become a legend in paranormal investigations, but now... Well... You're stuck in your office, bored and waiting for something exciting...`,
      `Oh wait! ${playerName}, you hear a notification from your email inbox...\nOpen it?`,
      `     <span class="text-bold text-blue-dark">Date:</span> 03 Sept 1999
            <span class="text-bold text-blue-dark">Sender:</span> Mel_UFO-Investigator_77

            Yo, ${playerName}, it's your buddy MELVIN from Evergreen!1! Hope you still REMEMBER me, space cowboy
            anyways, i just cant believe what im seeing... its NOT normal! noooo way. This is... PARA-NORMAL, and its HUUUGE.
            Like, REALLY f*cked up. I NEED your help here, at Evergreen!
            We need 2 meet @ <span class="text-yellow text-bold">Denver International Airport</span> tomorrow evening. plz dont be late. dont tell anyone about this.

            Cya,
            Melvin
            P.S. I''ve added <span class="text-yellow text-bold">$300</span> to your bank account for your plane ticket!1! HURRY UP!!
       `,
      `Hooray! A business trip!\nBefore leaving the office, don’t forget to take your Nokia from the desk. You’ll definitely need it.`
    ];

    const addNokiaToTheInvetory = async () => {
      try {
        await fetch("/inventory/add", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ item: 'Nokia' })
        });
      } catch (error) {
        console.error(error);
        throw error;
      }
    };
    addNokiaToTheInvetory();

    currentMessageIndex = 0;
    welcomeText.innerHTML = messages[0];
    updateContinueButtonText();
  };

  startButton.addEventListener("click", () => {
    indexScreen.style.display = "none";
    nameEntryScreen.style.display = "flex";
  });

  nameForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    playerName = playerNameInput.value.trim() || "Pekka";
    await createPlayer(playerName);
    nameEntryScreen.style.display = "none";
    welcomeScreen.style.display = "flex";
    initWelcomeScreen();
  });

  continueWelcomeButton.addEventListener("click", () => {
    currentMessageIndex++;
    if (currentMessageIndex < messages.length) {
      welcomeText.innerHTML = messages[currentMessageIndex];
      updateContinueButtonText();
    } else {
      window.location.href = "/menu";
    }
  });

  welcomeScreen.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      continueWelcomeButton.click();
    }
  });
});