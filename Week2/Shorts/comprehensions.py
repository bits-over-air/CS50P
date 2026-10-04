#empty dictionary , going to build up as we go 

def main():
    counts = {}
    words = get_words("/Users/vandana/Documents/Python/CS50P/Week2/Shorts/address.txt")
    lowercase_words = [ word.lower() for word in words if len(word) > 4]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}


    """for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1"""


    save_counts(counts)

main()
    