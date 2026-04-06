
import random
import time

while True:
    price = random.uniform(20000, 70000)
    difficulty = random.uniform(1, 3)
    energy = random.uniform(0.1, 0.5)

    profit = (price / difficulty) - energy * 120

    if profit > 0:
        action = "MINE"
    elif price < 30000:
        action = "BUY"
    else:
        action = "WAIT"

    print(f"AÇÃO: {action} | LUCRO: {profit:.2f}")
    time.sleep(2)

python ai.py

nano server.js

const http = require('http');

http.createServer((req, res) => {
  const actions = ["MINE","BUY","WAIT"];
  const response = {
    status: "IA ativa",
    action: actions[Math.floor(Math.random()*3)],
    profit: (Math.random()*100).toFixed(2)
  };

  res.writeHead(200, {'Content-Type': 'application/json'});
  res.end(JSON.stringify(response));
}).listen(3000);

console.log("Servidor rodando na porta 3000");

node server.js

npx create-expo-app app
cd app
npm start
import React, { useEffect, useState } from 'react';
import { View, Text } from 'react-native';

export default function App() {
  const [data, setData] = useState({});

  const fetchData = async () => {
    const res = await fetch('http://127.0.0.1:3000');
    const json = await res.json();
    setData(json);
  };

  useEffect(() => {
    setInterval(fetchData, 2000);
  }, []);

  return (
    <View style={{marginTop:50}}>
      <Text>🤖 {data.status}</Text>
import React, { useEffect, useState } from 'react';
import { View, Text } from 'react-native';

export default function App() {
  const [data, setData] = useState({});

  const fetchData = async () => {
    const res = await fetch('http://SEU_IP:3000');
    const json = await res.json();
    setData(json);
  };

  useEffect(() => {
    setInterval(fetchData, 3000);
  }, []);

  return (
    <View style={{marginTop:50}}>
      <Text>🤖 {data.status}</Text>
      <Text>💲 BTC: ${data.price}</Text>
      <Text>⚡ Ação: {data.action}</Text>
      <Text>💰 Lucro simulado: R$ {data.profit}</Text>
    </View>
  );
}      <Text>⚡ {data.action}</Text>
      <Text>💰 R$ {data.profit}</Text>
    </View>
  );
}

127.0.0.1

localhost

nano server.js



if (price < 25000) action = "BUY";
else if (price > 65000) action = "SELL";
else action = "WAIT";

nano server.js

const http = require('http');
const https = require('https');

let wallet = {
  balance: 1000, // dinheiro inicial (R$)
  btc: 0
};

function getBitcoinPrice(callback) {
  https.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd', (resp) => {
    let data = '';

    resp.on('data', chunk => data += chunk);
    resp.on('end', () => {
      const json = JSON.parse(data);
      callback(json.bitcoin.usd);
    });
  });
}

function decision(price) {
  if (price < 30000 && wallet.balance > 50) return "BUY";
  if (price > 60000 && wallet.btc > 0) return "SELL";
  return "HOLD";
}

http.createServer((req, res) => {

  getBitcoinPrice((price) => {

    let action = decision(price);

    if (action === "BUY") {
      let amount = wallet.balance * 0.2;
      wallet.btc += amount / price;
      wallet.balance -= amount;
    }

    if (action === "SELL") {
      let amount = wallet.btc * 0.5;
      wallet.balance += amount * price;
      wallet.btc -= amount;
    }

    const total = wallet.balance + (wallet.btc * price);

    const response = {
      status: "IA TRADER ATIVA",
      price: price,
      action: action,
      balance: wallet.balance.toFixed(2),
      btc: wallet.btc.toFixed(6),
      total: total.toFixed(2)
    };

    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(JSON.stringify(response));

  });

}).listen(3000);

console.log("🔥 IA INSANA rodando");

import React, { useEffect, useState } from 'react';
import { View, Text } from 'react-native';

export default function App() {
  const [data, setData] = useState({});

  const fetchData = async () => {
    const res = await fetch('http://SEU_IP:3000');
    const json = await res.json();
    setData(json);
  };

  useEffect(() => {
    setInterval(fetchData, 3000);
  }, []);

  return (
    <View style={{marginTop:50}}>
      <Text>🤖 {data.status}</Text>
      <Text>💲 BTC: ${data.price}</Text>

      <Text>⚡ Ação: {data.action}</Text>

      <Text>💵 Saldo: R$ {data.balance}</Text>
      <Text>🪙 BTC: {data.btc}</Text>

      <Text>📊 Total: R$ {data.total}</Text>
    </View>
  );
}

npm install react-native-chart-kit

import React, { useEffect, useState } from 'react';
import { View, Text, Dimensions } from 'react-native';
import { LineChart } from 'react-native-chart-kit';

export default function App() {
  const [data, setData] = useState({});
  const [prices, setPrices] = useState([]);

  const fetchData = async () => {
    const res = await fetch('http://SEU_IP:3000');
    const json = await res.json();

    setData(json);
    setPrices(prev => [...prev.slice(-9), json.price]);
  };

  useEffect(() => {
    setInterval(fetchData, 3000);
  }, []);

  return (
    <View style={{marginTop:50}}>
      <Text>🤖 {data.status}</Text>
      <Text>💲 BTC: ${data.price}</Text>

      <LineChart
        data={{
          labels: [],
          datasets: [{ data: prices.length ? prices : [0] }]
        }}
        width={Dimensions.get("window").width}
        height={220}
        yAxisLabel="$"
        chartConfig={{
          backgroundGradientFrom: "#000",
          backgroundGradientTo: "#000",
          color: () => "#00ff00"
        }}
      />

      <Text>⚡ {data.action}</Text>
      <Text>💵 R$ {data.balance}</Text>
      <Text>🪙 BTC {data.btc}</Text>
      <Text>📊 Total R$ {data.total}</Text>
    </View>
  );
}

let users = {};

if (req.url.startsWith('/login')) {
  const username = req.url.split('?user=')[1];

  if (!users[username]) {
    users[username] = {
      balance: 1000,
      btc: 0
    };
  }

  res.end(JSON.stringify(users[username]));
  return;
}

function decision(price, lastPrice) {
  if (!lastPrice) return "HOLD";

  if (price < lastPrice * 0.97) return "BUY";
  if (price > lastPrice * 1.05) return "SELL";

  return "HOLD";
}

npm install -g eas-cli

npx expo login

npx expo prebuild
npx expo run:android

npx expo build:android

[ SALDO TOTAL ]
[ GRÁFICO ]
[ AÇÃO DA IA ]
[ BOTÃO INVESTIR ]

NeuroMine X é um simulador avançado de investimentos com inteligência artificial.

Aprenda a tomar decisões no mercado de criptomoedas com um sistema inteligente que analisa dados em tempo real.

• Simulação de trading
• IA automática
• Gráficos em tempo real
• Sistema de carteira

Ideal para quem quer aprender e evoluir no mercado financeiro.

[ SALDO TOTAL ]
[ GRÁFICO AO VIVO ]
[ DECISÃO DA IA ]
[ BOTÃO INVESTIR ]
[ HISTÓRICO ]

🤖 IA: COMPRAR

Motivo:
- Queda de 6% nas últimas horas
- Região de oportunidade detectada

if (queda > 5%) → COMPRAR
if (alta > 8%) → VENDER
se estável → ESPERAR

[ 💰 SALDO TOTAL ]

[ 📈 GRÁFICO GRANDE ]

[ 🤖 DECISÃO DA IA ]
[ 📄 MOTIVO ]

[ 📊 HISTÓRICO ]

nano server.js

let lastPrice = null;

function decision(price) {
  let action = "HOLD";
  let reason = "Mercado estável";

  if (lastPrice) {
    let change = ((price - lastPrice) / lastPrice) * 100;

    if (change < -5) {
      action = "BUY";
      reason = `Queda de ${change.toFixed(2)}% → oportunidade`;
    }
    else if (change > 5) {
      action = "SELL";
      reason = `Alta de ${change.toFixed(2)}% → realização de lucro`;
    }
  }

  lastPrice = price;

  return { action, reason };
}

let history = [];

let { action, reason } = decision(price);

if (action === "BUY") {
  let amount = wallet.balance * 0.2;
  wallet.btc += amount / price;
  wallet.balance -= amount;
}

if (action === "SELL") {
  let amount = wallet.btc * 0.5;
  wallet.balance += amount * price;
  wallet.btc -= amount;
}

let total = wallet.balance + wallet.btc * price;

// salvar histórico
history.push({
  price,
  action,
  reason,
  total: total.toFixed(2)
});

if (history.length > 20) history.shift();

const response = {
  status: "IA PROFISSIONAL",
  price,
  action,
  reason,
  balance: wallet.balance.toFixed(2),
  btc: wallet.btc.toFixed(6),
  total: total.toFixed(2),
  history
};

import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView } from 'react-native';

export default function App() {
  const [data, setData] = useState({});

  const fetchData = async () => {
    const res = await fetch('http://SEU_IP:3000');
    const json = await res.json();
    setData(json);
  };

  useEffect(() => {
    setInterval(fetchData, 3000);
  }, []);

  return (
    <ScrollView style={{marginTop:50}}>

      <Text>🤖 {data.status}</Text>
      <Text>💲 BTC: ${data.price}</Text>

      <Text>⚡ Ação: {data.action}</Text>
      <Text>🧠 Motivo: {data.reason}</Text>

      <Text>💵 Saldo: R$ {data.balance}</Text>
      <Text>🪙 BTC: {data.btc}</Text>
      <Text>📊 Total: R$ {data.total}</Text>

      <Text>📜 Histórico:</Text>

      {data.history && data.history.map((item, index) => (
        <View key={index}>
          <Text>{item.action} | ${item.price}</Text>
          <Text>{item.reason}</Text>
        </View>
      ))}

    </ScrollView>
  );
}

/mobile-app (React Native)
   ├── App.js
   ├── components/
   ├── screens/

/backend (Node.js)
   ├── server.js
   ├── aiEngine.js
   ├── market.js
   ├── wallet.js
   ├── history.js


nano aiEngine.js

let lastPrices = [];

function movingAverage() {
  if (lastPrices.length < 5) return null;
  return lastPrices.reduce((a, b) => a + b, 0) / lastPrices.length;
}

function decision(price) {
  lastPrices.push(price);
  if (lastPrices.length > 10) lastPrices.shift();

  let action = "HOLD";
  let reason = "Mercado neutro";

  const avg = movingAverage();

  if (avg) {
    if (price < avg * 0.95) {
      action = "BUY";
      reason = "Preço abaixo da média → oportunidade";
    } 
    else if (price > avg * 1.05) {
      action = "SELL";
      reason = "Preço acima da média → lucro";
    }
  }

  return { action, reason, avg };
}

module.exports = { decision };

nano wallet.js

let wallet = {
  balance: 1000,
  btc: 0
};

function execute(action, price) {
  if (action === "BUY") {
    let amount = wallet.balance * 0.2;
    wallet.btc += amount / price;
    wallet.balance -= amount;
  }

  if (action === "SELL") {
    let amount = wallet.btc * 0.5;
    wallet.balance += amount * price;
    wallet.btc -= amount;
  }
}

function total(price) {
  return wallet.balance + wallet.btc * price;
}

module.exports = { wallet, execute, total };

nano history.js

let history = [];

function save(entry) {
  history.push(entry);
  if (history.length > 50) history.shift();
}

function getHistory() {
  return history;
}

module.exports = { save, getHistory };

nano server.js

const express = require('express');
const axios = require('axios');

const { decision } = require('./aiEngine');
const { wallet, execute, total } = require('./wallet');
const { save, getHistory } = require('./history');

const app = express();

app.get('/', async (req, res) => {
  try {
    const response = await axios.get(
      'https://api.coindesk.com/v1/bpi/currentprice.json'
    );

    const price = parseFloat(response.data.bpi.USD.rate.replace(',', ''));

    const { action, reason, avg } = decision(price);

    execute(action, price);

    const totalValue = total(price);

    save({
      price,
      action,
      reason,
      total: totalValue.toFixed(2)
    });

    res.json({
      status: "NEUROMINE X ELITE",
      price,
      action,
      reason,
      avg,
      balance: wallet.balance.toFixed(2),
      btc: wallet.btc.toFixed(6),
      total: totalValue.toFixed(2),
      history: getHistory()
    });

  } catch (err) {
    res.json({ error: "Erro ao buscar mercado" });
  }
});

app.listen(3000, () => console.log("Servidor rodando"));

npm install react-native-chart-kit

import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView } from 'react-native';
import { LineChart } from 'react-native-chart-kit';

export default function App() {
  const [data, setData] = useState({});

  const fetchData = async () => {
    const res = await fetch('http://SEU_IP:3000');
    const json = await res.json();
    setData(json);
  };

  useEffect(() => {
    setInterval(fetchData, 3000);
  }, []);

  return (
    <ScrollView style={{marginTop:50}}>

      <Text>🚀 {data.status}</Text>
      <Text>💲 BTC: ${data.price}</Text>

      <Text>🤖 {data.action}</Text>
      <Text>🧠 {data.reason}</Text>

      <Text>💵 Saldo: {data.balance}</Text>
      <Text>🪙 BTC: {data.btc}</Text>
      <Text>📊 Total: {data.total}</Text>

      {data.history && (
        <LineChart
          data={{
            labels: data.history.map((_, i) => i.toString()),
            datasets: [{ data: data.history.map(h => parseFloat(h.total)) }]
          }}
          width={350}
          height={200}
        />
      )}

      <Text>📜 Histórico:</Text>

      {data.history && data.history.map((item, i) => (
        <View key={i}>
          <Text>{item.action} - ${item.price}</Text>
          <Text>{item.reason}</Text>
        </View>
      ))}

    </ScrollView>
  );
}

import auth from '@react-native-firebase/auth';

auth()
  .createUserWithEmailAndPassword(email, senha)
  .then(() => console.log("Usuário criado"));

import auth from '@react-native-firebase/auth';

function registrar(email, senha) {
  return auth().createUserWithEmailAndPassword(email, senha);
}

function login(email, senha) {
  return auth().signInWithEmailAndPassword(email, senha);
}

import firestore from '@react-native-firebase/firestore';

const userId = auth().currentUser.uid;

firestore()
  .collection('users')
  .doc(userId)
  .set({
    balance: 1000,
    btc: 0,
    history: []
  });

https://seu-app.onrender.com

fetch('https://seu-app.onrender.com')

[ 💰 SALDO ]
[ 📈 GRÁFICO ]
[ 🤖 IA + MOTIVO ]
[ 📜 HISTÓRICO ]

npx expo build:android

pkg update && pkg upgrade
pkg install nodejs git

node -v

mkdir neuromine
cd neuromine

npm init -y
npm install express axios

nano server.js

const express = require('express');
const axios = require('axios');

const app = express();

let wallet = {
  balance: 1000,
  btc: 0
};

let history = [];
let prices = [];

function movingAverage() {
  if (prices.length < 5) return null;
  return prices.reduce((a, b) => a + b, 0) / prices.length;
}

function decision(price) {
  prices.push(price);
  if (prices.length > 10) prices.shift();

  let action = "HOLD";
  let reason = "Mercado neutro";

  const avg = movingAverage();

  if (avg) {
    if (price < avg * 0.95) {
      action = "BUY";
      reason = "Preço abaixo da média";
    } 
    else if (price > avg * 1.05) {
      action = "SELL";
      reason = "Preço acima da média";
    }
  }

  return { action, reason };
}

app.get('/', async (req, res) => {
  try {
    const r = await axios.get(
      'https://api.coindesk.com/v1/bpi/currentprice.json'
    );

    const price = parseFloat(r.data.bpi.USD.rate.replace(',', ''));

    const { action, reason } = decision(price);

    if (action === "BUY") {
      let amount = wallet.balance * 0.2;
      wallet.btc += amount / price;
      wallet.balance -= amount;
    }

    if (action === "SELL") {
      let amount = wallet.btc * 0.5;
      wallet.balance += amount * price;
      wallet.btc -= amount;
    }

    let total = wallet.balance + wallet.btc * price;

    history.push({
      price,
      action,
      reason,
      total: total.toFixed(2)
    });

    if (history.length > 20) history.shift();

    res.json({
      status: "NEUROMINE X",
      price,
      action,
      reason,
      balance: wallet.balance.toFixed(2),
      btc: wallet.btc.toFixed(6),
      total: total.toFixed(2),
      history
    });

  } catch {
    res.json({ error: "erro api" });
  }
});

app.listen(3000, () => console.log("Rodando na porta 3000"));

node server.js

http://localhost:3000

npm install -g expo-cli

npx create-expo-app app
cd app
npm install react-native-chart-kit

npx expo start

nano App.js

import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView } from 'react-native';

export default function App() {
  const [data, setData] = useState({});

  const fetchData = async () => {
    const res = await fetch('http://SEU_IP:3000');
    const json = await res.json();
    setData(json);
  };

  useEffect(() => {
    setInterval(fetchData, 3000);
  }, []);

  return (
    <ScrollView style={{marginTop:50}}>
      <Text>🚀 {data.status}</Text>
      <Text>💲 BTC: {data.price}</Text>

      <Text>🤖 {data.action}</Text>
      <Text>🧠 {data.reason}</Text>

      <Text>💵 {data.balance}</Text>
      <Text>🪙 {data.btc}</Text>
      <Text>📊 {data.total}</Text>

      <Text>📜 Histórico:</Text>

      {data.history && data.history.map((item, i) => (
        <View key={i}>
          <Text>{item.action} - {item.price}</Text>
          <Text>{item.reason}</Text>
        </View>
      ))}

    </ScrollView>
  );
}

SEU_IP

ip a

192.168.x.x

node server.js

pkg install nodejs

node -v

npm install express axios

nano server.js

const r = await axios.get(
  'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
);

const price = parseFloat(r.data.price);

pkill node

curl http://localhost:3000

{
  "status": "NEUROMINE X",
  "price": ...
}

ls

nano server.js

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.json({ ok: true });
});

app.listen(3000, () => console.log("Rodando na porta 3000"));

Y

node

ENTER


CTRL + X


