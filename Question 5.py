def longest_un_word(filename):
    longest_word = ""
    special_chars = ".,';?!\n"

    with open(filename) as f:
        for line in f:
            line = line.lower()  # make everything lowercase

            for c in special_chars:  # remove special characters
                line = line.replace(c, "")

            words = line.split(" ")  # extract words

            for word in words:
                if len(word) == 0:
                    continue

                # check if word starts with "un"
                if word[:2] == "un":
                    # check if it is longer than current longest
                    if len(word) > len(longest_word):
                        longest_word = word

    return longest_word


# run the function
print(longest_un_word("book1.txt"))
