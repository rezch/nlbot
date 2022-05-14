import telebot

from os import remove
from TxtToMp3 import Mp3Convert

from messages_list import LANGUAGES, COMMANDS, MESSAGES_LIST
from db_operator import *

"""
    TODO:
    1) delete command range input
    2) commands args in the line
    3) notification command
"""


token = '5320394418:AAECLQlJyDMVPTHAljjMbG3AmrOpwQ0TQVA'

bot = telebot.TeleBot(token=token, parse_mode=None)

TEXT_SIZE = 60
LIST_SIZE = 200

UNDEFINED = 'UNDEFINED1DfXYLA2oeO4iTE7R4cScGwd6eHkCg'


@bot.message_handler(commands=COMMANDS["help"])
def help_command(message):
    log(message)

    bot.send_message(
        chat_id=message.chat.id,
        text=message_text("help", message)
    )


@bot.message_handler(commands=COMMANDS["list_voice"])
def list_voice_command(message):
    log(message)

    user_id = str(message.from_user.id)

    file_name = user_id + ".mp3"

    lang = UsersData.users[user_id]['language']

    user_data_list = UsersData.users[user_id]['data_list']

    if len(user_data_list) == 0:
        bot.send_message(
            chat_id=message.chat.id,
            text=message_text("list_is_empty", message)
        )
    else:
        text = ""
        for value in user_data_list:
            text += value + '. '

        convert = Mp3Convert(text, lang, user_id)
        convert.convert()

        with open(file_name, 'rb') as f:
            bot.send_audio(
                chat_id=message.chat.id,
                audio=f
            )

        remove(file_name)


@bot.message_handler(commands=["test"])
def test_command(message):
    print(message.text)


@bot.message_handler(commands=COMMANDS['delete'])
def delete_command(message):
    log(message)

    user_id = str(message.from_user.id)

    user_data_list = UsersData.users[user_id]['data_list']

    if len(user_data_list) == 0:
        bot.send_message(
            chat_id=message.chat.id,
            text=message_text("list_is_empty", message)
        )
    else:
        echo = bot.send_message(
            chat_id=message.chat.id,
            text=message_text("delete", message)
        )
        bot.register_next_step_handler(message=echo, callback=delete_command_echo)


def delete_command_echo(message):
    text = str(message.text)

    user_id = str(message.from_user.id)

    user_data_list = UsersData.users[user_id]['data_list']

    if text == "*":
        echo = bot.send_message(
            chat_id=message.chat.id,
            text=message_text("accept", message)
        )

        bot.register_next_step_handler(message=echo, callback=accept_delete_command)
    else:
        try:
            text = list(map(int, text.split()))

            if max(text) > len(user_data_list) or min(text) < 1:
                bot.send_message(
                    chat_id=message.chat.id,
                    text=message_text("delete_number_exc", message, [1, len(user_data_list)])
                )
            else:
                for i in text:
                    user_data_list[i - 1] = UNDEFINED

                user_data_list = [value for value in user_data_list if value != UNDEFINED]

                UsersData.users[user_id]['data_list'] = user_data_list

                push_db_user(bot, message)
            
        except TypeError:
            bot.send_message(
                chat_id=message.chat.id,
                text=message_text("input_exc", message)
            )
    

def accept_delete_command(message):
    text = str(message.text)

    user_id = str(message.from_user.id)

    if text in ['yes', 'да']:
        user_data_list = []

        UsersData.users[user_id]['data_list'] = user_data_list

        push_db_user(bot, message)
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=message_text("unaccept", message)
        )


@bot.message_handler(commands=COMMANDS['add'])
def add_command(message):
    log(message)

    echo = bot.send_message(
        chat_id=message.chat.id, 
        text=message_text('add', message)
    )
    bot.register_next_step_handler(message=echo, callback=echo_add_command)


def echo_add_command(message):
    text = str(message.text)

    if len(text) >= TEXT_SIZE:
        bot.send_message(
            chat_id=message.chat.id, 
            text=message_text("add_text_exc", message, [len(text)])
        )
        return

    user_data_list = UsersData.users[str(message.from_user.id)]['data_list']

    if len(user_data_list) >= LIST_SIZE:
        bot.send_message(
            chat_id=message.chat.id,
             text=message_text("add_size_exc", message, [len(user_data_list)])
        )
    else:
        user_data_list.append(text)

        UsersData.users[str(message.from_user.id)]['data_list'] = user_data_list

        push_db_user(bot, message)


@bot.message_handler(commands=COMMANDS["list"])
def get_list_command(message):
    log(message)
    
    user_data_list = UsersData.users[str(message.from_user.id)]['data_list']

    text = message_text("list", message, user_data_list)

    if len(user_data_list) == 0:
        bot.send_message(
            chat_id=message.chat.id,
            text=message_text("list_is_empty", message)
        )
    else:
        for i, value in enumerate(user_data_list):
            text += str(i + 1) + ": " + value + "\n"

        bot.send_message(
            chat_id=message.chat.id,
            text=text
        )


@bot.message_handler(commands=COMMANDS['hello'])
def send_hello(message):
    log(message)

    bot.reply_to(
        message,
        message_text('hello', message, [message.from_user.username])
    )


@bot.message_handler(commands=['start'])
def start_command(message):
    log(message)

    language = message.from_user.language_code 
    language = language if language in LANGUAGES else "EN"

    username = message.from_user.username

    UsersData(message.from_user.id, username, language)

    bot.reply_to(
        message, 
        text=message_text("start", message, username)
    )


@bot.message_handler(commands=['lang'])
def language_command(message):
    log(message)

    echo = bot.send_message(
        chat_id=message.chat.id, 
        text=message_text("language_choose", message, LANGUAGES)
    )
    bot.register_next_step_handler(message=echo, callback=echo_set_language)


def echo_set_language(message):
    text = str(message.text).lower()

    for lang in UsersData.languages:
        for option in UsersData.languages[lang]:
            if option == text:
                set_language(message.from_user.id, lang)

                return bot.send_message(chat_id=message.chat.id, text=message_text("language_set", message))
        
    bot.send_message(
        chat_id=message.chat.id, 
        text=message_text("input_exc", message)
    )

def start():
    UsersData.db_init()

    bot.infinity_polling()


if __name__ == "__main__":
    start()

