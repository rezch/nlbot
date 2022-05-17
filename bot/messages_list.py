LANGUAGES = ["en", "ru"]

LANGUAGES_NAMES = [
    'Русский ', 'English '
]

LANGUAGES_VARIATIONS = {
    'en': ['en', 'english', 'eng'],
    'ru': ['ru', 'rus', 'russian', 'рус', 'русский']
}

COMMANDS = {
  "hello": ["hello", "привет"],
  "add": ["add", "добавить", "добавь"],
  "list": ["list", "список"],
  "list_voice": ["say", "voice", "скажи"],
  "delete": ["delete", "del", "уд", "удали", "удалить"],
  "help": ["help", "помощь", "commands", "команды"]
}


MESSAGES_LIST = {
    "help": {
        "en": "I can create note lists.\n" +
            "To add a new note, enter /add.\n" +
            "Enter /list to see your list of notes.\n" +
            "To delete unnecessary notes, use the /delete command.\n" +
            "If you need to listen to the texts of the notes, enter /say, and I will send a voice message.",
        "ru": "Я могу создават списки заметок.\n" +
            "Для добавления новой заметки введи /добавить.\n" +
            "Введи /список, чтобы увидеть свой список заметок\n" +
            "Чтобы удалить ненужные заметки используй команду /удали\n" +
            "Если нужно прослушать тексты записок введи /скажи, и я отправлю голосовое сообщение."
    },
    "start": {
        "en": "Hi, I'm Buy List Bot!\nI can help you take notes and create lists!\nUse command: " + 
                    "/help to find out what I can do.",
        "ru": "Привет, Я Buy List Bot!\nЯ могу помочь тебе делать заметки и создавать списки. Напиши: " +
                    "/помощь чтобы узнать что я могу."
    },
    "hello": {
        "en": "Hello {}!",
        "ru": "Привет {}!"
    },
    "language_choose": {
        "en": "Choose one of the languages: " + "{} " * len(LANGUAGES),
        "ru": "Выбрерите один из языков: " + "{} " * len(LANGUAGES)
    },
    "language_set": {
        'en': 'Selected language: english',
        'ru': 'Выбран язык: русский',
    },
    "add": {
        "en": "What do you want to add to the list?",
        "ru": "Что вы хотите добавить в список?"
    },
    "add_text_exc": {
        "en": "The note must be no longer than 60 characters, you have entered {}",
        "ru": "Заметка должно быть не длиннее 60 символов, вы ввели {}"
    },
    "add_size_exc": {
        "en": "The number of notes you have added to the list should not exceed {}",
        "ru": "Количество добавленных вами заметок в список вещей не должно превышать {}"
    },
    "done": {
        "en": "Done!",
        "ru": "Выполнено!"
    },
    "fault": {
        "en": "An error occurred while executing the command, please try again later :(",
        "ru": "При выполнении команды произошла ошибка, попробуйте позже :("
    },
    "list": {
        "en": "Here is your list of notes, if you want me to voice it to you, write /say\n",
        "ru": "Вот ваш список заметок, если вы хотите, чтобы я его озвучил его вам, напишите /скажи\n"
    },
    "delete": {
        "en": 'Enter the note numbers separated by a space or "*" - to delete the entire list',
        "ru": 'Ввежите номера заметок через пробел или "*" - для удаления всего списка'
    },
    "accept": {
        "en": "Are you sure about it?",
        "ru": "Вы уверены в этом?"
    },
    "unaccept": {
        "en": "Action canceled",
        "ru": "Действие отменено"
    },
    "delete_number_exc": {
        "en": "Note numbers should be from {} to {}",
        "ru": "Номера заметкок должны быть от {} до {}"
    },
    "input_exc": {
        "en": "Incorrect input, try again",
        "ru": "Неправильный ввод, попробуйте еще"
    },
    "list_is_empty": {
        "en": "Your notes list is empty. Write /add to add new note",
        "ru": "Ваш список заметок пуст. Введите /добавить чтобы добавить заметку"
    }
}

