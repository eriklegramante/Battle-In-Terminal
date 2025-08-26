# ⚔️ Battle Game / Jogo de Batalha (Terminal Edition)

A small **terminal-based battle game** written in Python.  
Este é um pequeno **jogo de batalha no terminal** escrito em Python.  

The project was made to practice **programming logic** and **English skills**.  
Este projeto foi feito para praticar **lógica de programação** e **inglês**.  

The game is **playable on any machine** directly from the terminal.  
O jogo é **jogável em qualquer máquina** diretamente no terminal.  

It is modularized and organized into folders for better readability and scalability.  
Ele é modularizado e organizado em pastas para melhor leitura e escalabilidade.  

---

## ⚙️ Requirements / Requisitos

- Python 3.8+
- The following libraries (already listed in the `requirements.txt` inside the project folder):  
  - `colorama`  
  - Any other dependencies you add  

Para instalar as dependências:  

```bash
pip install -r requirements.txt
```

---

## 🗂 Project Structure / Estrutura do Projeto

```
battle-game/
│── src/
│   ├── main.py            # Entry point / Ponto de entrada
│   ├── character.py       # Character class and logic / Classe e lógica dos personagens
│   ├── battle.py          # Manual/automatic battle functions / Funções de batalha manual/automática
│   ├── cards.py           # Magic cards system / Sistema de cartas mágicas
│   └── utils.py           # Helpers (e.g. dividers, status)
│
│── requirements.txt       # Dependencies / Dependências
│── README.md              # Documentation / Documentação
```

---

## ▶️ How to Run / Como Executar

Inside the project folder, open your terminal and run:  
Dentro da pasta do projeto, abra o terminal e rode:  

```bash
python src/main.py
```

---

## 🎮 How to Play / Como Jogar

1. **Choose your nickname / Escolha seu apelido**  
   - Both players type their nicknames.  
   - Ambos os jogadores digitam seus apelidos.  

2. **Battle begins / A batalha começa** ⚔️  
   - Randomly decides who starts.  
   - Decide aleatoriamente quem começa.  

3. **Your turn / Seu turno** 🔄  
   - `1` → **Attack / Atacar** (normal attack, increases stamina).  
   - `2` → **Use Magic Card / Usar Carta Mágica** (requires ≥ 50 stamina).  
   - `3` → **Exit / Sair** (you give up, other player wins).  

4. **Stamina system / Sistema de Stamina** 💥  
   - Attacks increase stamina.  
   - Ao atacar, você aumenta a stamina.  
   - At ≥ 50, you can use a Magic Card.  
   - Com 50 ou mais, você pode usar Carta Mágica.  

5. **Victory conditions / Condições de Vitória** 🏆  
   - Game continues until one player’s life = 0.  
   - O jogo continua até que a vida de um chegue a 0.  
   - Survivor wins!  
   - O sobrevivente vence!  

---

## 📝 Notes / Notas

- Runs fully in the **terminal**.  
- Roda totalmente no **terminal**.  
- Uses colors/icons for fun (via `colorama`).  
- Usa cores/ícones para diversão (via `colorama`).  
- Modularized code for learning.  
- Código modular para aprendizado.  
