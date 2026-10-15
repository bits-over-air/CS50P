import emoji
emojis = input("Input:")
emojis = emojis.strip()
print(emoji.emojize(emojis, language ="alias"))