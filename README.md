# EmojiTyping
Just my first package, probably for easy emoji outputs(no ascii codes or finding emojis in the emoji tab)



Define an emoji class with `your_class_name = EmojiPrinter()`, if you have the import set to `from Emojitypes.typemoji import *`

Works best with pycharm.


## Note

When using the random emoji list function inside of the emoji printer, you will sometimes get a repr() version of an emoji. 
For example, sometimes it will output `🐦\u200d🔥`, which is the repr() of the phoenix emoji. This can be solved with
`" ".join(your_emoji_printer_name.random_list(length)`. This is only for print() and input() functions

(may happen in tkinter as well)
