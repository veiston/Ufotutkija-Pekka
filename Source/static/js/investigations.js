document.addEventListener("DOMContentLoaded", () => {
    const updateStep = async (step) => {
        try {
            const response = await fetch("/investigations/update-step", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ step }),
            });
            const data = await response.json();
            console.log(data);
            return data;
        } catch (error) {
            console.error(error);
        }
    };

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

    function showStoryModal(text, onClose) {
        showModal({
            message: text,
            buttons: [{ label: "OK", value: true }],
            onClose: onClose,
        });
    }

    const createCreatureCard = (value, onClick) => {
        const article = document.createElement("card");
        article.className = "card";

        const wrapper = document.createElement("div");
        wrapper.className = "card__wrapper";

        const figure = document.createElement("figure");
        const img = document.createElement("img");
        img.src = `/static/images/character_art/${value.image}`;
        img.alt = "Creature";
        figure.appendChild(img);

        const content = document.createElement("div");
        content.className = "card__content";

        const h2 = document.createElement("h2");
        h2.textContent = value.title;

        const p = document.createElement("p");
        p.textContent = value.text;

        content.appendChild(h2);
        content.appendChild(p);

        wrapper.appendChild(figure);
        wrapper.appendChild(content);
        article.appendChild(wrapper);

        article.addEventListener("click", onClick);

        return article;
    };

    const createActionButton = (value, key, onClick) => {
        const button = document.createElement("button");
        button.className =
            key === "examine" ? "button" : "button button--gray-light";
        button.textContent = value.text;
        button.addEventListener("click", onClick);

        return button;
    };

    const createItemCard = (value) => {
        const item = document.createElement("div");
        item.className = "product-item";

        const article = document.createElement("article");

        const title = document.createElement("h3");
        title.className = "product-title";
        title.innerHTML = value.amount
            ? `${value.name}<br>(${value.amount})`
            : value.name;

        const img = document.createElement("img");
        img.className = "product-image";
        img.src = `/static/images/investigations/${value.name}.png`;
        img.alt = value.name;

        article.appendChild(img);
        article.appendChild(title);
        item.appendChild(article);

        return item;
    };

    const startInvestigation = async () => {
        let currentStep = null;
        let story = null;
        let turnsLeft = 0;

        const textContainer = document.getElementById("investigationText");
        const actionsContainer = document.getElementById("investigationActions");
        const cityContainer = document.getElementById("investigationCity");
        const backContainer = document.getElementById("backImg");

        const urlParams = new URLSearchParams(window.location.search);
        const resultParam = urlParams.get('result');

        if (resultParam) {
            story = await fetchInvestigation();

            if (!story) {
                textContainer.textContent = "Error loading investigation.";
                return;
            }

            cityContainer.innerText = story.city;
            backContainer.style.backgroundImage = `url("/static/images/investigations/${story.ident}.png")`;

            if (resultParam === 'win') {
                showStoryModal(story.win_text, async () => {
                    await updateStep(null);
                    window.location.href = "/menu";
                });
            } else if (resultParam === 'lose') {
                showStoryModal(story.lose_text, () => {
                    window.location.href = "/menu";
                });
            }
            return;
        }

        const renderStep = async (stepNumber) => {
            if (!turnsLeft) {
                window.location.href = "/combat";
                return;
            }

            const stepData = story.steps[stepNumber];

            textContainer.innerHTML = stepData.is_examined
                ? "“There’s nothing more interesting here. Better check other places.”"
                : stepData.text;

            actionsContainer.innerHTML = "";

            Object.entries(stepData.choices)
                .reverse()
                .forEach(([key, value]) => {
                    if (key === "examine" && stepData.is_examined) {
                        return;
                    }
                    if (stepData.choices[key].is_creature) {
                        const creatureCard = createCreatureCard(value, async () => {
                            currentStep = value.next_step;
                            const updateData = await updateStep(currentStep);
                            turnsLeft = updateData?.turns_limit;

                            if (currentStep) {
                                await renderStep(currentStep);
                            }
                        });
                        actionsContainer.appendChild(creatureCard);
                    } else {
                        const actionButton = createActionButton(
                            value,
                            key,
                            async () => {
                                if (key === "examine") {
                                    const resultData = await handleExamineClick();
                                    currentStep = resultData.is_last
                                        ? value.next_step
                                        : story.step;
                                } else {
                                    currentStep = value.next_step;
                                }

                                const updateData = await updateStep(currentStep);
                                turnsLeft = updateData?.turns_limit;
                                const isWin = updateData.is_win;
                                story = updateData.story;
                                if (isWin) {
                                    showStoryModal(story.win_text, () => {
                                        window.location.href = "/menu";
                                    });
                                    return;
                                }

                                if (currentStep) {
                                    await renderStep(currentStep);
                                }
                            }
                        );
                        actionsContainer.appendChild(actionButton);
                    }
                });
        };

        story = await fetchInvestigation();

        if (!story) {
            textContainer.textContent = "Error loading investigation.";
            return;
        }

        cityContainer.innerText = story.city;
        backContainer.style.backgroundImage = `url("/static/images/investigations/${story.ident}.png")`;
        currentStep = story.step;
        turnsLeft = story.turns_limit;

        if (story?.description) {
            showStoryModal(story.description, renderStep(currentStep));
        } else {
            renderStep(currentStep);
        }
    };

    const fetchInvestigation = async () => {
        try {
            const response = await fetch("/investigations/start");
            return await response.json();
        } catch (error) {
            console.error(error);
            return null;
        }
    };

    const startExamination = async (itemName, resolve) => {
        try {
            const response = await fetch("/investigations/examine", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ item_name: itemName }),
            });

            const result = await response.json();

            showModal({
                message: result.result,
                buttons: [{ label: "OK", value: true }],
                onClose: resolve,
            });

            return result;
        } catch (error) {
            console.error(error);
        }
    };

    const handleExamineClick = async () => {
        const inventory = await fetchInventory();

        const actionsContainer = document.getElementById("investigationActions");
        actionsContainer.innerHTML = "";

        const textContainer = document.getElementById("investigationText");
        textContainer.innerHTML = `<p>Let's take a look at what they're trying to hide.</p>
        <p style="color: white; opacity: 0.7; font-style: italic;">(Use equipment from your inventory to investigate the location and identify the type of creature.)</p>`;

        const promises = [];
        let result = null;

        Object.entries(inventory)
            .reverse()
            .forEach(([key, value]) => {
                if (value.name === "Coffee") {
                    return;
                }

                const item = createItemCard(value);

                const promise = new Promise((resolve) => {
                    item.addEventListener("click", async () => {
                        result = await startExamination(value.name, resolve);
                    });
                });
                actionsContainer.appendChild(item);

                promises.push(promise);
            });

        await Promise.race(promises);
        return result;
    };

    startInvestigation();
});