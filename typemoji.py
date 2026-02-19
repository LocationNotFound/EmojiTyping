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
        print(get_emoji(key))

    def return_ascii(filler, key:str):
        return ord(get_emoji(key))




