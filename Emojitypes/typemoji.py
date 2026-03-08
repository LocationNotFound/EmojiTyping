import random
from Emojitypes.settings import *
from Emojitypes.Errors import *
from Emojitypes.Emojilist.lists import *

def get_emoji(key):
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

    def emoji_fr_ascii(filler, ascii):
        if len(str(ascii)) > EMOJIWARNINGLENGTH:
            raise EmojiAsciiWarning("Using chr(ascii) may be more efficient")
        return chr(ascii)

    def random(filler):
        random_value = random.choice(list(emoji_list.values()))
        return random_value

    def random_list(filler, length:int):
        random_list = []
        for i in range(length):
            random_list.append(random.choice(list(emoji_list.values())))
        return random_list

    def help(filler):
        for keys, values in emoji_list.items():
            print(f'{keys} -> {values}')
    #currently in progress
    def change_max_length(filler, new_length:int):
        change_key_max_length(new_length)

    def get(filler, key:str):
        if len(key) > KEY_MAX_LENGTH:
            raise KeyToLongError("Key is too long")
        return get_emoji(key)


class EmojiList(list):
    def __new__(cls, *args):
        reresult = []
        for pos, i in enumerate(args):
            if type(i) != str:
                raise TypeError("Emoji key should be a string")

            elif i not in emoji_list.keys():
                raise KeyError(f"Emoji {i} in slice {pos} not found")

            else:
                reresult.append(emoji_list[i])

        return reresult












