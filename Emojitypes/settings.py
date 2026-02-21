#settings

KEY_MAX_LENGTH = 20
EMOJIWARNINGLENGTH = 4

def change_key_max_length(new_length:int):
    #bad practice, but is easy enough right now
    global KEY_MAX_LENGTH
    KEY_MAX_LENGTH = new_length
