import json

from messages_list import MESSAGES_LIST


DB_PATH = "db/data.json"


def message_text(msg_type, message, args=None):
    language = UsersData.users[str(message.from_user.id)]["language"]
    
    if args:
        text = MESSAGES_LIST[msg_type][language].format(*args)
    else:
        text = MESSAGES_LIST[msg_type][language]
       
    return text



class DBError(Exception):
    def __str__(self):
        return "Cannot load DB, check existing of json file"


class BotFilesError(Exception):
    def __str__(self):
        return "The necessary files cannot be loaded. Check the integrity of the directory"


def set_language(user_id, lang):
    UsersData.users[str(user_id)]["language"] = lang
    
    push_db()


def push_db():
    try:
        with open(DB_PATH, 'r+') as f:
            db = json.load(f)
            
            db['users'] = UsersData.users
            
            f.seek(0)
            json.dump(db, f)
            f.truncate()

    except FileNotFoundError:
        raise DBError()


def push_db_user(bot, message):
    try:
        push_db()
        
        bot.send_message(
            chat_id=message.chat.id,
            text=message_text("done", message)
        )
    except DBError:
        bot.send_message(
            chat_id=message.chat.id,
            text=message_text("fault", message)
        )


class UsersData:
    users = {}
    users_id = []

    languages_list = [
        'Русский ', 'English '
    ]

    languages = {
        'en': ['en', 'english', 'eng'],
        'ru': ['ru', 'rus', 'russian', 'рус', 'русский']
    }

    @staticmethod
    def db_init():
        try:
            with open(DB_PATH, 'r') as f:
                UsersData.users = json.load(f)['users']
                
                UsersData.users_id = list(UsersData.users.keys())
        except FileNotFoundError:
            raise DBError()

    def __init__(self, user_id, name, language):
        user_id = str(user_id)
        
        if user_id not in UsersData.users_id:
            self.user = {
                "name": str(name),
                "language": language,
                "data_list": []
            }
            
            UsersData.users_id.append(user_id)
            
            UsersData.users[user_id] = self.user


def log(message):
    print(message.from_user.id, message.from_user.username)
    print(message.id, message.date)
    print(message.text)
    print("<-------------------->")

