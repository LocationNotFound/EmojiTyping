import random
from settings import *
from Errors import KeyToLongError

emoji_list = {"waving_hand":"👋",
        "clapping_hands":"👏",
        "raised_hand":"✋",
        "victory_hand":"✌️",
        "pinched_fingers":"🤌",
        "korean_finger_heart":"🫰",
        "vulcan_salute":"🖖",
        "ok_hand":"👌",
        "heart_hands":"🫶",
        "thumbs_up":"👍",
        "thumbs_down":"👎",
        "crossed_fingers":"🤞"
        }

def get_emoji(key):
    global emoji_list
    try:
        return emoji_list[key]
    except Exception:
        print("Emoji not found")


class EmojiPrinter():
    #for less typing
    def type(filler, key:str, end="\n"):
        if len(key) > KEY_MAX_LENGTH:
            raise KeyToLongError("Key is too long")
        print(get_emoji(key), end=end)

    def return_ascii(filler, key:str):
        return ord(get_emoji(key))


    def random(filler):
        global emoji_list
        random_value = random.choice(list(emoji_list.values()))
        return random_value
    #currently in progress
    def change_max_length(filler, new_length:int):
        change_key_max_length(new_length)

