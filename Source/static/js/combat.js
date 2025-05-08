document.addEventListener("DOMContentLoaded", () => {
  const sel = (s) => document.querySelector(s);
  const selAll = (s) => Array.from(document.querySelectorAll(s));
  const e = {
    playerHp: sel("#playerHp"),
    enemyHp: sel("#enemyHp"),
    log: sel("#log"),
    controls: sel(".menu__controls"),
    itemMenu: sel("#itemMenu"),
    itemList: sel("#itemList"),
    playerSprite: sel("#playerSprite"),
    enemySprite: sel("#enemySprite"),
  };
  const sfx = {
    attack: new Audio("/static/audio/attack.mp3"),
    hit: new Audio("/static/audio/hit.mp3"),
    item: new Audio("/static/audio/item.mp3"),
  };

  let player = { hp: 200, max: 200, atk: 25 },
    enemy = {
      hp: 150,
      max: 150,
      atk: 20,
      /* set defaults in case load fails */
      weak: "Salt",
      name: "Alien",
      sprite: "alien.png",
    },
    inv = [];
  let storyStep = null,
    victoryText = null;

  const randCrit = () => Math.random() < 0.05;
  const updateBars = () => {
    e.playerHp.style.width = `${(player.hp / player.max) * 100}%`;
    e.enemyHp.style.width = `${(enemy.hp / enemy.max) * 100}%`;
  };
  const log = (m) => {
    const p = document.createElement("p");
    p.textContent = m;
    e.log.prepend(p);
  };
  const animateHit = (el) => {
    el.classList.add("hit");
    setTimeout(() => el.classList.remove("hit"), 300);
  };
  const setEnemyDisplay = () => {
    const s = document.getElementById("enemySprite");
    const n = document.querySelector(".enemy .name-tag");
    if (s) s.src = `/static/images/character_art/${enemy.sprite}`;
    if (n) n.textContent = enemy.name;
  };
  // Fetches all combat data for the current fight
  const fetchCombatData = async () => {
    const d = await (await fetch("/combat/current-step")).json();
    storyStep = d.step;
    let invData = d.investigation;
    let c =
      invData && invData.creature_data ? invData.creature_data : invData || d;
    /* set defaults in case load fails */
    enemy.name = c.name || c.creature || d.creature_name || d.name || "Alien";
    enemy.weak =
      c.weakness || c.weak || d.creature_weakness || d.weakness || "Salt";
    enemy.sprite = c.sprite || d.creature_sprite || d.sprite || "alien.png";
    enemy.hp = c.hp || d.creature_hp || d.hp || 150;
    enemy.max = c.hp || d.creature_hp || d.hp || 150;
    victoryText =
      invData && invData.win_text ? invData.win_text : d.win_text || null;
    setEnemyDisplay();
  };
  const fetchInv = async () => {
    inv = await (await fetch("/inventory/items")).json();
  };
  const consumeItem = async (item) => {
    await fetch("/inventory/delete", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ item }),
    });
    await fetchInv();
  };
  const useItem = async (name) => {
    e.itemMenu.classList.remove("show");
    sfx.item.play();
    if (name === "Coffee") {
      player.hp = Math.min(player.max, player.hp + 50);
      log("Paranit 50 HP.");
      await consumeItem(name);
      updateBars();
      enemyTurn();
      return;
    }
    let pwr = 30;
    if (name === enemy.weak) {
      pwr *= 2;
      log("Critical damage dealt to the enemy!");
    }
    if (randCrit()) {
      pwr *= 2;
      log("Critical hit!");
    }
    animateHit(e.playerSprite);
    enemy.hp = Math.max(0, enemy.hp - pwr);
    sfx.hit.play();
    log(`Item deals ${pwr} damage.`);
    await consumeItem(name);
    updateBars();
    enemyTurn();
  };
  const openItems = () => {
    e.itemList.innerHTML = inv
      .map((n) => `<li data-item="${n.name}" style="cursor: pointer">${n.name}</li>`)
      .join("");
    e.itemMenu.classList.add("show");
  };
  e.itemMenu.addEventListener("click", (e1) => {
    if (e1.target.tagName === "LI") useItem(e1.target.dataset.item);
    if (e1.target === e.itemMenu) e.itemMenu.classList.remove("show");
  });
  e.controls.addEventListener("click", (e1) => {
    const b = e1.target.closest(".menu__button");
    if (!b) return;
    const a = b.dataset.action;
    if (a === "attack") {
      animateHit(e.playerSprite);
      sfx.attack.play();
      let dmg = player.atk * (randCrit() ? 2 : 1);
      if (dmg > player.atk) log("Critical hit!");
      enemy.hp = Math.max(0, enemy.hp - dmg);
      log(`Item deals ${dmg} damage.`);
      updateBars();
      enemyTurn();
    }
    if (a === "item") openItems();
    if (a === "inspect")
      log(`${enemy.name} ${enemy.hp}/${enemy.max} HP, heikko: ${enemy.weak}.`);
  });
  // Handles enemy's turn and checks for win/lose
  const enemyTurn = () => {
    if (enemy.hp <= 0) return endBattle(true);
    setTimeout(() => {
      animateHit(e.enemySprite);
      let dmg = enemy.atk * (randCrit() ? 2 : 1);
      if (dmg > enemy.atk) log("UFO strikes critically!");
      player.hp = Math.max(0, player.hp - dmg);
      sfx.hit.play();
      log(`Item deals ${dmg} damage.`);
      updateBars();
      if (player.hp <= 0) endBattle(false);
    }, 800);
  };
  // Shows modal and updates story after battle
  const endBattle = (won) => {
    selAll(".menu__button").forEach((b) => (b.disabled = true));
    const sfxEnd = new Audio(
      won ? "/static/audio/victory.mp3" : "/static/audio/defeat.mp3"
    );
    sfxEnd.play();
    let message =
      won && victoryText
        ? victoryText
        : won
        ? "You won the battle! You are a hero!"
        : "You lost the battle... Rest and try again.";
    showModal({
      message,
      buttons: [{ label: "OK", value: true }],
      onClose: async (_) => {
         window.location.href = `/investigations?result=${won ? "win" : "lose"}`
        // await updateStory(won);
        // window.location.href = "/travel";
      },
      disableBackdropClose: true,
      disableEscClose: true,
    });
    setTimeout(() => {
      const okBtn = document.querySelector("#modalBoxButtons button");
      if (okBtn) okBtn.focus();
    }, 100);
  };
  // const updateStory = async (won) => {
  //   await fetch("/investigations/update-step", {
  //     method: "POST",
  //     headers: { "Content-Type": "application/json" },
  //     body: JSON.stringify({
  //       step: storyStep,
  //       combat_result: won ? "win" : "lose",
  //       complete: won,
  //     }),
  //   });
  // };
  (async () => {
    await fetchInv();
    await fetchCombatData();
    updateBars();
    const music = document.getElementById("battleMusic");
    if (music) {
      music.muted = false;
      music.volume = 1;
      music.play().catch(() => {});
    }
  })();
});
