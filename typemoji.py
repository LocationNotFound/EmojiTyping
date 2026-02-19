from settings import *

from Errors import KeyToLongError


def get_emoji(key):
    global emoji_list
    emoji_list = {"waving_hand":"👋",
        "clapping_hands":"👏",
        }
    try:
        return emoji_list[key]
    except Exception:
        print("Emoji not found")


class emoji_printer():
    #for less typing
    def type(filler, key:str):
        if len(key) > KEY_MAX_LENGTH:
            raise KeyToLongError("Key is too long")
        print(get_emoji(key))

    def return_ascii(filler, key:str):
        return ord(get_emoji(key))

    #currently in progress
    def change_max_length(filler, new_length:int):
        debug.change_key_max_length(new_length)






