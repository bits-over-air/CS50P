def main():
    text = input("Enter any text with emoticons: ")
    emojis = convert(text)
    print(emojis)

def convert(text):
        text = text.replace(":)","\U0001F642")
        text = text.replace(":(","\U0001F641")
        return text

main()
