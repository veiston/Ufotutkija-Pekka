'use strict';

const playerMoneyText = document.querySelector('#playerMoney');
const dealerHand = document.querySelector('#dealerHand');
const playerHand = document.querySelector('#playerHand');
const dealerScore = document.querySelector('#dealerScore');
const playerScore = document.querySelector('#playerScore');
const cardBack = 'static/images/cards/Back.png';
const hit = document.querySelector('#hit');
const doubleDown = document.querySelector('#doubleDown');
const stand = document.querySelector('#stand');
const betInput = document.querySelector('#betInput');
const freeMoneyTxt = document.querySelector('#freeMoney');

const player = {score:0,hand:[]};
const dealer = {score:0,hand:[]};
let playerStand = false;
let dealerStand = false;
let playerBust = false;
let dealerBust = false;
let deck = [];


//betInput.addEventListener('')



/*
const fetchPlayer = async () => {
  try {
    const response = await fetch("/player/detail");
    return await response.json();
  } catch (error) {
    console.error(error);
    return null;
  }
};
console.log(fetchPlayer().money);
const handleMoney = async (money) => {
  try {
    await new Promise((resolve) => setTimeout(resolve, 500));
    const response = await fetch("/player/update", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({money}),
    });
    if (!response.ok) throw new Error("Failed to update location");
  } catch (error) {
    console.error(error);
  }
};*/

//playerMoneyText.innerText = fetchPlayer().money;
//console.log(fetchPlayer());
function createDeck(){
  const deck = [
                                      {name:'Ace of Spades',value:'A',src:'static/images/cards/Spades_Ace.png'},
                                      {name:'Two of Spades',value:2,src:'static/images/cards/Spades_2.png'},
                                      {name:'Three of Spades',value:3,src:'static/images/cards/Spades_3.png'},
                                      {name:'Four of Spades',value:4,src:'static/images/cards/Spades_4.png'},
                                      {name:'Five of Spades',value:5,src:'static/images/cards/Spades_5.png'},
                                      {name:'Six of Spades',value:6,src:'static/images/cards/Spades_6.png'},
                                      {name:'Seven of Spades',value:7,src:'static/images/cards/Spades_7.png'},
                                      {name:'Eight of Spades',value:8,src:'static/images/cards/Spades_8.png'},
                                      {name:'Nine of Spades',value:9,src:'static/images/cards/Spades_9.png'},
                                      {name:'Ten of Spades',value:10,src:'static/images/cards/Spades_10.png'},
                                      {name:'Jack of Spades',value:10,src:'static/images/cards/Spades_Jack.png'},
                                      {name:'Queen of Spades',value:10,src:'static/images/cards/Spades_Queen.png'},
                                      {name:'King of Spades',value:10,src:'static/images/cards/Spades_King.png'},

                                      {name:'Ace of Hearts',value:'A',src:'static/images/cards/Hearts_Ace.png'},
                                      {name:'Two of Hearts',value:2,src:'static/images/cards/Hearts_2.png'},
                                      {name:'Three of Hearts',value:3,src:'static/images/cards/Hearts_3.png'},
                                      {name:'Four of Hearts',value:4,src:'static/images/cards/Hearts_4.png'},
                                      {name:'Five of Hearts',value:5,src:'static/images/cards/Hearts_5.png'},
                                      {name:'Six of Hearts',value:6,src:'static/images/cards/Hearts_6.png'},
                                      {name:'Seven of Hearts',value:7,src:'static/images/cards/Hearts_7.png'},
                                      {name:'Eight of Hearts',value:8,src:'static/images/cards/Hearts_8.png'},
                                      {name:'Nine of Hearts',value:9,src:'static/images/cards/Hearts_9.png'},
                                      {name:'Ten of Hearts',value:10,src:'static/images/cards/Hearts_10.png'},
                                      {name:'Jack of Hearts',value:10,src:'static/images/cards/Hearts_Jack.png'},
                                      {name:'Queen of Hearts',value:10,src:'static/images/cards/Hearts_Queen.png'},
                                      {name:'King of Hearts',value:10,src:'static/images/cards/Hearts_King.png'},

                                      {name:'Ace of Clubs',value:'A',src:'static/images/cards/Clubs_Ace.png'},
                                      {name:'Two of Clubs',value:2,src:'static/images/cards/Clubs_2.png'},
                                      {name:'Three of Clubs',value:3,src:'static/images/cards/Clubs_3.png'},
                                      {name:'Four of Clubs',value:4,src:'static/images/cards/Clubs_4.png'},
                                      {name:'Five of Clubs',value:5,src:'static/images/cards/Clubs_5.png'},
                                      {name:'Six of Clubs',value:6,src:'static/images/cards/Clubs_6.png'},
                                      {name:'Seven of Clubs',value:7,src:'static/images/cards/Clubs_7.png'},
                                      {name:'Eight of Clubs',value:8,src:'static/images/cards/Clubs_8.png'},
                                      {name:'Nine of Clubs',value:9,src:'static/images/cards/Clubs_9.png'},
                                      {name:'Ten of Clubs',value:10,src:'static/images/cards/Clubs_10.png'},
                                      {name:'Jack of Clubs',value:10,src:'static/images/cards/Clubs_Jack.png'},
                                      {name:'Queen of Clubs',value:10,src:'static/images/cards/Clubs_Queen.png'},
                                      {name:'King of Clubs',value:10,src:'static/images/cards/Clubs_King.png'},

                                      {name:'Ace of Diamonds',value:'A',src:'static/images/cards/Diamonds_Ace.png'},
                                      {name:'Two of Diamonds',value:2,src:'static/images/cards/Diamonds_2.png'},
                                      {name:'Three of Diamonds',value:3,src:'static/images/cards/Diamonds_3.png'},
                                      {name:'Four of Diamonds',value:4,src:'static/images/cards/Diamonds_4.png'},
                                      {name:'Five of Diamonds',value:5,src:'static/images/cards/Diamonds_5.png'},
                                      {name:'Six of Diamonds',value:6,src:'static/images/cards/Diamonds_6.png'},
                                      {name:'Seven of Diamonds',value:7,src:'static/images/cards/Diamonds_7.png'},
                                      {name:'Eight of Diamonds',value:8,src:'static/images/cards/Diamonds_8.png'},
                                      {name:'Nine of Diamonds',value:9,src:'static/images/cards/Diamonds_9.png'},
                                      {name:'Ten of Diamonds',value:10,src:'static/images/cards/Diamonds_10.png'},
                                      {name:'Jack of Diamonds',value:10,src:'static/images/cards/Diamonds_Jack.png'},
                                      {name:'Queen of Diamonds',value:10,src:'static/images/cards/Diamonds_Queen.png'},
                                      {name:'King of Diamonds',value:10,src:'static/images/cards/Diamonds_King.png'}
                                      ];
  return deck;
}

hit.addEventListener('click', function(){buttonPress('hit');});
doubleDown.addEventListener('click', function(){buttonPress('doubleDown');});
stand.addEventListener('click', function(){buttonPress('stand');});

/*
    async function loadPlayerData() {
        try {
            const response = await fetch('/player/detail');
            const playerData = await response.json();
            //const moneyEl = document.getElementById('money');
            playerMoneyText.textContent = playerData.money;
        } catch (error) {
            console.error(error);
        }
    }
loadPlayerData();
*/
    const fetchPlayer = async () => {
        try {
            const response = await fetch("/player/detail");
            return await response.json();
        } catch (error) {
            console.error(error);
            return null;
        }
    };
  //let playerInfo = await fetchPlayer();
  //console.log(playerInfo.money);
async function testaus(){
  const playerInfo = await fetchPlayer();
  console.log(playerInfo.money);
  handleMoney(playerInfo.money-5);
}
//testaus();
    const handleMoney = async (money) => {
        try {
            await new Promise((resolve) => setTimeout(resolve, 500));
            const response = await fetch("/player/update", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({money}),
            });
            if (!response.ok) throw new Error("Failed to update location");
        } catch (error) {
            console.error(error);
        }
    };




//Fisher-Yates shuffle nicked from Courey Wong
//https://coureywong.medium.com/how-to-shuffle-an-array-of-items-in-javascript-39b9efe4b567
function shuffle(d) {
  let i = d.length, j, temp;
  while (--i > 0) {
    j = Math.floor(Math.random() * (i + 1));
    temp = d[j];
    d[j] = d[i];
    d[i] = temp;
  }
  return d;
}
//I know this is a bit extra since blackjack uses very few cards
//but I like when games are "honest"


function ace(card, score){
  if (card === 'A') {
    if (score+11<=21){
      return 11;
    } else {
      return 1;
    }
  } else {
    return card;
  }
}

function checkStatus(value, who){
  if(value>21){
    switch (who){
      case 'player':
        playerBust = true;
        //hiddenCardReveal();
        //console.log('REVEAL THE DAMN CARD');
        break;
      case 'dealer':
        dealerBust = true;
        //hiddenCardReveal();
    }
  } else if(value>=17 && who==='dealer'){
    dealerStand = true;
    console.log('dingdingding');
  }
}

function hiddenCardReveal(){
  document.querySelector('#hiddenCard').src = dealer.hand[0].src;
  console.log(dealer.score);
  dealerScore.innerText = dealer.score;
}

function clear(){
  playerStand = false;
  dealerStand = false;
  playerBust = false;
  dealerBust = false;
  deck = [];
  player.score = 0;
  player.hand = [];
  dealer.score = 0;
  dealer.hand = [];
  //playerHand.innerHTML = '';
  //playerScore.innerHTML = '';
  //dealerHand.innerHTML = '';
  //dealerScore.innerHTML = '';
  console.log(player);
}

function endCondition(){
  if((playerBust) || (playerStand && dealerStand)){
    if((playerBust && dealerBust) || player.score === dealer.score){
      console.log('draw: you get your money back');
      hiddenCardReveal();
      clear();
      return;
    } else if(dealerBust || (player.score>dealer.score && !playerBust)){
      console.log('you win! you get 2x your bet');
      hiddenCardReveal();
      clear();
      return;
    } else {
      console.log('you lose.');
      hiddenCardReveal();
      clear();
      return;
    }
  }

  if(playerStand && (!dealerStand || !dealerBust)) {
    deal();
  }
}



function deal(){

  if(!playerStand) {
    player.hand.push(deck.shift());
    const playerCard = player.hand[player.hand.length-1];
    player.score+=ace(playerCard.value,player.score);
    checkStatus(player.score, 'player');

    const img = document.createElement('img');
    img.src=playerCard.src;
    img.className = 'card';
    playerHand.appendChild(img);
    playerScore.innerText=player.score;
  }

  if(!dealerStand){
    dealer.hand.push(deck.shift());
    const dealerCard = dealer.hand[dealer.hand.length-1];
    dealer.score+=ace(dealerCard.value,dealer.score);
    checkStatus(dealer.score,'dealer');

    const img = document.createElement('img');
    if(dealer.hand.length<2) {
      img.src = cardBack;
      img.id = 'hiddenCard';
      dealerScore.innerText='?';
    } else {
      img.src = dealerCard.src;
      dealerScore.innerText=`${dealer.score-ace(dealer.hand[0].value, 0)}+?`;
      console.log('real score: '+dealer.score+' dealer hand value: '+dealer.hand[0].value);
    }
    img.className = 'card';
    dealerHand.appendChild(img);
  }

  endCondition();
}

function startGame(){
  deck = createDeck();
  shuffle(deck);
  console.log(deck[1]);
  deal();
  console.log(deck[1]);

  deal();
}

function buttonPress(choice) {
  switch(choice){
    case 'hit':
      console.log('hit');
      deal();
      break;
    case 'doubleDown':
      //currently this doesn't do anything sensible
      //might remove later
      console.log('double');
      playerStand = true;
      hiddenCardReveal();
      deal();
      break;
    case 'stand':
      playerStand = true;
      console.log('stand');
      hiddenCardReveal();
      deal();

  }
}

async function freebie(){
  let playerInfo = await fetchPlayer();
  console.log(playerInfo.money);
  let newMoney = playerInfo.money+5;
  handleMoney(newMoney);
  freeMoneyTxt.innerText = 'Here, have 5$ on the house!';
  //playerInfo = await fetchPlayer();
  //console.log(playerInfo.money);
  playerMoneyText.innerText = `Money: ${newMoney}`;
}
freebie();
//startGame();
//console.log(await loadPlayerData());