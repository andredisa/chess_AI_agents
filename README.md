# ♟️ Chess AI Agents

>Welcome to **chess AI agents** — an interactive AI vs AI chess game built with **Streamlit**, **Python-Chess**, and **AutoGen** (OpenAI). Two powerful language models face off on the board, making moves in real time, while you watch the strategy unfold! 🤖⚔️🤖


---

## 🚀 Features

- ✅ AI vs AI chess match powered by GPT models
- ✅ Real-time chessboard visualization with SVG rendering
- ✅ User-friendly web interface via Streamlit
- ✅ Game coordination via AutoGen's ConversableAgent framework
- ✅ Full move history and end-of-game detection (checkmate, stalemate, etc.)
- ✅ Configurable number of turns and full reset capability
- ✅ Modular, clean codebase for easy extension

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/andredisa/chess_AI_agents.git
cd chess_AI_agents
```

### 2. Create a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```bash
chess_AI_agents/
├── app.py              # 🚀 Main Streamlit app that runs the interface and integrates all components.
├── config/        # 📂 Configuration files.
│   └── settings.py     # 🛠️ Contains settings
├── agents/        # 📂 Agent-related files.
│   ├── base.py         # 🧠 Abstract class for all chess agents.
│   └── game_agents.py  # 🤖 Concrete AI chess agents.
├── chess_logic/   # 📂 Chess game logic.
│   ├── board_utils.py  # ⚙️ Chessboard utilities (e.g., move validation).
│   └── game_state.py   # 🕹️ Tracks game state (checkmate, stalemate).
├── ui/            # 📂 User interface components.
│   └── sidebar.py      # 📝 Sidebar for user configuration (API keys, settings).
├── utils/         # 📂 General utilities.
│   └── session.py      # ⏳ Manages session state and interactions.
├── requirements.txt    # 📜 Python dependencies.
├── README.md           # 📄 Project documentation.
└── LICENSE          # 📝 MIT License.


```

---

## 🔑 Requirements

- Python 3.8+
- An **OpenAI API key**
- An **Internet connection** to access OpenAI models (GPT-4o or GPT-3.5-turbo)

---

## 🧠 How It Works

- Two agents (`Agent_White` and `Agent_Black`) are powered by **OpenAI LLMs** using **AutoGen**.
- A **Game_Master** agent handles validation and game coordination.
- Each agent queries available moves, selects one, and executes it.
- The board state is visualized after each move.
- The user configures the number of moves and watches the AI play!

---

## 💻 Running the App

Run the Streamlit app with:

```bash
streamlit run app.py
```
> Then open http://localhost:8501 in your browser.

---

## ⚙️ Configuration
- 🔐 Enter your **OpenAI API key** in the sidebar

- ♟️ Choose the **number of turns** (recommended: 5–10 for demo)

    - You can also set the default number of turns in the config file:
        > In `config/settings.py`, modify the constant:
        ```python
        DEFAULT_MAX_TURNS = 5
        ```


- ▶️ Click **Start Game** to begin the AI chess match

---

## 🛠️ Future Improvements
- 🎮 Add **human** vs **AI mode**

- 📄 **PGN** export of games

- 🤖 **Local model support** (e.g., LLaMA, Mistral)

- 🔁 Multiple **game modes** and **agent personalities**

--- 

## ✨ Contributing

🎉 **Contributions are more than welcome!**

If you find a bug 🐞, have a feature request ✨, or want to improve the code 💻:

- Open an [Issue](https://github.com/andredisa/chess_AI_agents/issues)  
- Submit a [Pull Request](https://github.com/andredisa/chess_AI_agents/pulls) 🚀  

>💬 Feel free to reach out on [GitHub](https://github.com/andredisa) or by [email](mailto:andreadisanti22@gmail.com)!

Let’s build this together!

---

## 📜 License

📄 This project is released under the **MIT License**.  
Please refer to the [LICENSE](LICENSE) file for full details.

---

### 🧑‍💻✨ Happy coding
