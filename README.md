# SheinBot - Telegram Bot for Shein Products

<img src="https://github.com/ghaiith/Youtube-to-Mp3-TelegramBot/blob/main/Examples/1.PNG " width="200">
<img src="https://github.com/ghaiith/Youtube-to-Mp3-TelegramBot/blob/main/Examples/2.PNG " width="200">
<img src="https://github.com/ghaiith/Youtube-to-Mp3-TelegramBot/blob/main/Examples/3.PNG " width="200">
<img src="https://github.com/ghaiith/Youtube-to-Mp3-TelegramBot/blob/main/Examples/4.PNG " width="200">

SheinBot is a Telegram bot that allows you to search for products on Shein using keywords. It utilizes the Shein API to fetch product details and provides you with information about the products along with images.

## Features

- Search for products on Shein using keywords.
- View product details such as title and price.
- See product images and available colors.

## How to Use

To use SheinBot, follow the steps below:

1. **Create a Telegram Bot:**
   - If you don't have a Telegram bot, you can create one by talking to the [BotFather](https://t.me/botfather) on Telegram. Follow these steps:
     - Open Telegram and search for "BotFather."
     - Start a chat with BotFather and use the `/newbot` command.
     - BotFather will ask for a name for your bot. Choose a name for your SheinBot (e.g., "MySheinBot").
     - BotFather will then ask for a username for your bot. The username must end with "bot" (e.g., "MySheinBot_bot").
     - Once your bot is created, BotFather will provide you with a bot token. Save this token; you will need it later.

2. **Get the Shein API Key:**
   - To access the Shein API, you need an API key from the RapidAPI platform. Follow these steps:
     - Sign up or log in to your RapidAPI account.
     - Subscribe to the "Unofficial Shein" API to obtain the API key.
     - Save the API key for later use.

3. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/shein-telegram-bot.git
   cd shein-telegram-bot
   ```

4. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Configure the Bot:**
   - Open the `bot.py` file and replace `YOUR_TELEGRAM_BOT_TOKEN` with the Telegram bot token obtained from BotFather.
   - Replace `YOUR_RAPIDAPI_KEY` with the Shein API key obtained from the RapidAPI platform.

6. **Run the Bot:**
   ```
   python bot.py
   ```

7. **Interact with the Bot:**
   - Open Telegram and search for your bot's username (e.g., `@MySheinBot_bot`).
   - Start a chat with the bot and send it a product keyword to search for products on Shein.
   - The bot will provide you with product details, images, and available colors (if any).

## Contributing

We welcome contributions from the community to make SheinBot even better. To contribute, follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository (`git clone https://github.com/your-username/shein-telegram-bot.git`).
3. Create a new branch for your feature or bug fix (`git checkout -b new-feature`).
4. Make your changes and commit them (`git commit -m "Add new feature"`).
5. Push the changes to your forked repository (`git push origin new-feature`).
6. Open a pull request on the original repository and describe your changes in detail.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This Telegram bot is developed using the unofficial Shein API. It is not affiliated with or endorsed by Shein or Telegram. Use it at your own risk.

---

![SheinBot Screenshot](sheinbot_screenshot.png)

You can copy the content above and replace `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_RAPIDAPI_KEY` with your actual bot token and Shein API key, respectively. The updated README includes a logo and a screenshot to make it more visually appealing. Additionally, it provides clear instructions on how to contribute to the project, making it easier for others to get involved. Feel free to further customize the README to fit your project's style and needs.