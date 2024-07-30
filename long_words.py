INPUT_PATH = "DATA/words.txt"
OUTPUT_PATH = "long_words.txt"
MIN_LENGTH = 20

with open(INPUT_PATH) as words_in:
    with open(OUTPUT_PATH, "w") as words_out:
        # open another output file here ....
        for raw_word in words_in:
            word = raw_word.rstrip()
            if len(word) > MIN_LENGTH:
                words_out.write(raw_word)
