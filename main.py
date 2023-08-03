import requests
import telebot

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token obtained from BotFather on Telegram.
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Shein API endpoint and headers
SHEIN_API_URL = "https://unofficial-shein.p.rapidapi.com/products/search"
SHEIN_API_HEADERS = {
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
    "X-RapidAPI-Host": "unofficial-shein.p.rapidapi.com"
}

def search_shein_product(keywords):
    querystring = {
        "keywords": keywords,
        "language": "ar",
        "country": "US",
        "currency": "USD",
        "sort": "7",
        "limit": "5",
        "page": "1"
    }

    response = requests.get(SHEIN_API_URL, headers=SHEIN_API_HEADERS, params=querystring)
    data = response.json()
    return data['info']['products']

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me the product keyword, and I'll find it for you.")

@bot.message_handler(func=lambda message: True)
def handle_search_product(message):
    keywords = message.text
    if keywords.startswith('SKU: '):
        keywords = keywords[6:]

    try:
        products = search_shein_product(keywords)
        if not products:
            bot.reply_to(message, "No products found.")
            return

        for product in products:
            title = product['goods_name']
            price = product.get('retailPrice', {}).get('amountWithSymbol', 'N/A')
            image = product['goods_img']
            result_text = f"Title: {title}\nPrice: {price}\n\n"
            bot.send_photo(message.chat.id, image, caption=result_text)

            # Send additional images in a media group
            pos_images = product['detail_image']
            media_group = [telebot.types.InputMediaPhoto(image_url) for image_url in pos_images]
            bot.send_media_group(message.chat.id, media_group)

            # Send available colors if any
            colors = {}
            pos_images = product['relatedColor']
            if pos_images:
                bot.send_message(message.chat.id, "Available colors:")
                for color in pos_images:
                    color_price = color['retailPrice']['amountWithSymbol']
                    color_images = color["detail_image"]
                    media_group = [telebot.types.InputMediaPhoto(image_url) for image_url in color_images]
                    bot.send_media_group(message.chat.id, media_group)
                    bot.send_message(message.chat.id, f"Color Price: {color_price}")

    except Exception as e:
        bot.reply_to(message, "Sorry, an error occurred while processing your request.")

if __name__ == "__main__":
    bot.polling()
