document.addEventListener("DOMContentLoaded", () => {
    function getImageSrc(name) {
        return `/static/images/items/${name}.png`;
    }

    async function loadShopItems() {
        try {
            const response = await fetch('/shop/items');
            const items = await response.json();

            const productList = document.querySelector('.product-list');
            productList.innerHTML = '';

            items.forEach(item => {
                const li = document.createElement('li');
                li.className = 'product-item';

                const article = document.createElement('article');

                const title = document.createElement('h3');
                title.className = 'product-title';
                title.textContent = item.name;

                const img = document.createElement('img');
                img.className = 'product-image';
                img.src = getImageSrc(item.name);
                img.alt = item.name + ' icon';

                const price = document.createElement('p');
                price.className = 'product-subtitle';
                price.textContent = 'Price: $' + (item.price ?? 0);

                article.appendChild(title);
                article.appendChild(img);
                article.appendChild(price);

                const buyButton = document.createElement('button');
                buyButton.className = 'button button--gray-light';
                buyButton.textContent = 'Buy';
                buyButton.addEventListener('click', (e) => {
                    e.stopPropagation();
                    buyNewItem(item.name);
                });

                article.appendChild(buyButton);

                li.appendChild(article);

                productList.appendChild(li);
            });
        } catch (error) {
            console.error(error);
        }
    }

    async function loadPlayerData() {
        try {
            const response = await fetch('/player/detail');
            const playerData = await response.json();
            const moneyEl = document.getElementById('money');
            moneyEl.textContent = playerData.money;
        } catch (error) {
            console.error(error);
        }
    }

    async function buyNewItem(name) {
        try {
            const response = await fetch('/shop/buy', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ item_name: name })
            });

            const result = await response.json();
            console.log(result);

            if (result.error === "Insufficient funds") {
                showModal({
                    message: "Not enough money! Want to try your luck?",
                    buttons: [
                        { label: "Step into the Lucky Room", value: "gamble", className: "button button--red-white" },
                        { label: "No, I’m not 18 yet", value: "cancel" }
                    ],
                    onClose: (value) => {
                        if (value === "gamble") {
                            window.location.href = "/blackjack";
                        }
                    }
                });
                return;
            }

            showModal({
                message: result.message || "Cha-ching! Another questionable purchase made",
                buttons: [{ label: "OK", value: true }],
                onClose: async () => {
                    await loadPlayerData();
                    await loadShopItems();
                }
            });
        } catch (error) {
            console.error(error);
        }
    }

    function goToMainMenu() {
        window.location.href = "/menu";
    }

    const fetchInventory = async () => {
        try {
            const response = await fetch("/inventory/items");
            const data = (await response.json()) || [];
            console.log(data);
            return data;
        } catch (error) {
            console.error(error);
        }
    };

    async function start() {
        await loadShopItems();
        await loadPlayerData();
    }

    document.getElementById("menuButton").addEventListener("click", goToMainMenu);
    document.getElementById("inventoryButton").addEventListener("click", async () => {
        const inventory = await fetchInventory();

        const filteredInventory = inventory.filter(item => item.name !== "Nokia");

        let inventoryHtml = "";
        if (filteredInventory?.length) {
            filteredInventory.forEach(item => {
                inventoryHtml += `
                  <li class="product-item product-item--no-action">
                      <article>
                            <img class="product-image" src="${getImageSrc(item.name)}" alt="${item.name} icon">
                          <h3 class="product-title">${item.name}</h3>
                          <p class="product-subtitle">${item.amount ?? 0} pcs</p>
                      </article>
                  </li>
              `;
            });
        } else {
            inventoryHtml = "Empty life, empty soul... empty shopping cart too?"
        }

        showModal({
            message: filteredInventory?.length ? `<ul class="product-list product-list--no-wrap">${inventoryHtml}</ul>` : inventoryHtml,
            buttons: [{ label: "OK", value: true }],
            onClose: () => {
            }
        });
    });
    start();
});