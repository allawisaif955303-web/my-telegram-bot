import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# التوكن الخاص بك
TOKEN = '8262177659:AAHdcjnfDMU7vhPwLw4E_TC-QsMtQVI5zMQ'
bot = telebot.TeleBot(TOKEN)

# دالة لإنشاء الأزرار الرئيسية
def get_main_menu():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton('👤 Profile')
    btn2 = KeyboardButton('💰 Balance')
    btn3 = KeyboardButton('⛏ Mine')
    btn4 = KeyboardButton('⚙️ Settings')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# التعامل مع أمر start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to OM Crypto Bot! Use the menu below:", reply_markup=get_main_menu())

# التعامل مع الأزرار والنصوص
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '👤 Profile':
        bot.send_message(message.chat.id, "👤 Your Profile:\nName: User\nLevel: 1")
    elif message.text == '💰 Balance':
        bot.send_message(message.chat.id, "💰 Your current balance: 0.00 BTC")
    elif message.text == '⛏ Mine':
        bot.send_message(message.chat.id, "⛏ Mining process started... 🚀")
    elif message.text == '⚙️ Settings':
        bot.send_message(message.chat.id, "⚙️ Settings Menu is currently empty.")
    else:
        bot.send_message(message.chat.id, "I don't understand this command. Please use the buttons.")

print("Bot is running...")
bot.polling(none_stop=True)
