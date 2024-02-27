## Telegram Chat Bot

## Description

This Python script implements a simple chatbot using the Telegram Bot API and the `telegram` library. The chatbot responds to commands and messages sent by users on Telegram. It provides a basic framework for building more complex chatbots with additional functionality.

### Features

- **Command Handlers:** Responds to commands such as `/start`, `/help`, and `/custom`.
- **Message Handler:** Responds to user messages with predefined or custom responses.
- **Group Message Handling:** Responds differently to messages in groups versus private chats.
- **Debugging Information:** Prints debug information about incoming messages and bot responses.

## Usage

1. Create a new bot with BotFather on Telegram and obtain an API token.
2. Replace the `TOKEN` variable in the script with the API token provided by BotFather.
3. Customize the `bot` variable with your bot's username.
4. Run the script.
5. Interact with the bot by sending commands or messages on Telegram.

## Requirements

- Python 3.x
- `python-telegram-bot` library

## Instructions

1. Clone or download the project from GitHub:

    ```bash
    git clone https://github.com/yourusername/telegram-chat-bot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd telegram-chat-bot
    ```

3. Install the required dependencies:

    ```bash
    pip install python-telegram-bot
    ```

4. Edit the script (`chat_bot.py`) and replace `TOKEN` with your bot's API token.

5. Run the bot script:

    ```bash
    python bot.py
    ```

6. Interact with the bot on Telegram.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Author

YASSINE LAHSSINI 👻
- GitHub: [yassinsl](https://github.com/yassinsl)
