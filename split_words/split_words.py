from justifytext import justify

with open('/Users/afoix/dango-git/python-challenge/split_words/text.txt') as text:
    string = text.read()
    split_words = string.split(' ')

    # One where all the text is spaced to 40 characters
    bugdet_user = int(input("Tell me a budget: "))
    budget_char = bugdet_user
    words_line = []
    for word in split_words:
        if len(word) >= budget_char:
            words_line_space = ' '.join(words_line)
            words_line_justified = justify(words_line_space, bugdet_user, justify_last_line = True)
            print(' '.join(words_line_justified), end="\n")

            # Print output file
            output_file = open("myfile" + "%s.txt" % bugdet_user, "a")
            output_file.write(' '.join(words_line_justified) + "\n")

            # reset teh counters
            budget_char = bugdet_user
            words_line = []

        else:
            words_line.append(word)
            budget_char = budget_char - len(word) - 1










