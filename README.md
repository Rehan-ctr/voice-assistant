# 🎙️ Voice Assistant

A Python-based voice assistant that listens for a wake word and executes voice commands to open popular websites. Built using speech recognition and text-to-speech technologies.

## ✨ Features

- **Wake Word Activation** — Say **"Google"** to activate the assistant.
- **Voice Commands** — Open websites like Google, YouTube, Facebook, and WhatsApp using natural speech.
- **Text-to-Speech Feedback** — The assistant speaks back to confirm actions.
- **Ambient Noise Adjustment** — Automatically adapts to background noise for better accuracy.
- **Continuous Listening** — Runs in a loop, always ready for the next command.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [pyttsx3](https://pypi.org/project/pyttsx3/) | Offline text-to-speech conversion |
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) | Microphone input & speech-to-text via Google API |
| [webbrowser](https://docs.python.org/3/library/webbrowser.html) | Opening URLs in the default browser |

## 📋 Prerequisites

- **Python 3.7+**
- A working **microphone**
- An active **internet connection** (required for Google Speech Recognition API)

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Rehan-ctr/voice-assistant.git
   cd voice-assistant
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   ```

   Activate it:

   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**

   ```bash
   pip install pyttsx3 SpeechRecognition PyAudio
   ```

   > **Note (Windows):** If `PyAudio` fails to install, download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually:
   > ```bash
   > pip install PyAudio‑0.2.14‑cp311‑cp311‑win_amd64.whl
   > ```

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

### How It Works

1. The assistant starts and greets you: *"Hey, how can I help you?"*
2. It continuously listens for the wake word **"Google"**.
3. Once it hears the wake word, it responds and waits for a command.
4. Supported commands:

   | Voice Command | Action |
   |---|---|
   | *"Open Google"* | Opens [google.com](https://google.com) |
   | *"Open YouTube"* | Opens [youtube.com](https://youtube.com) |
   | *"Open Facebook"* | Opens [facebook.com](https://facebook.com) |
   | *"Open WhatsApp"* | Opens [whatsapp.com](https://whatsapp.com) |

5. If the command is not recognized, the assistant will say *"Command not recognized"*.

## 📁 Project Structure

```
voice-assistant/
├── main.py          # Main application entry point
├── .gitignore       # Git ignore rules
└── README.md        # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Here are some ideas for improvement:

- Add more voice commands (e.g., play music, check weather, set timers)
- Integrate with an AI API (e.g., Gemini, OpenAI) for conversational responses
- Add a GUI interface
- Support for multiple languages

To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Rehan** — [@Rehan-ctr](https://github.com/Rehan-ctr)
